from functools import partial

from tracuni.define.type import (
    Rule,
    Destination,
    DestinationSection,
    Origin,
    OriginSection,
    Stage,
    PipeCommand,
)
from tracuni.schema.builtin.pipe import (
    ext_tracer_out_point,
    ext_tracer_path,
    pipe_head,
    pipe_sep_string,
    pipe_catch_essential,
    pipe_mask_secret,
    pipe_dump,
    pipe_cut,
    ext_api_kind,
    pipe_inject_headers,
    ext_out_headers,
)


ruleset = (
    Rule(
        description="Записать заголовки в запрос",
        destination=Destination(DestinationSection.POINT_ARGS, 'message'),
        pipeline=(
            partial(pipe_inject_headers, **{'prefix_key': 'context_headers'}),
        ),
        origins=(
            Origin(
                OriginSection.SPAN, None,
            ),
            Origin(
                OriginSection.POINT_ARGS, ext_out_headers,
            ),
            Origin(
                OriginSection.ADAPTER,
                lambda adapter: adapter.config.service_name,
            ),
        ),
        stage=Stage.PRE,
    ),
    Rule(
        description="Наименование партнерского сервиса сохранить для "
                    "переиспользования",
        destination=Destination(
            DestinationSection.REUSE,
            'peer_name',
          ),
        pipeline=(
            pipe_head,
            lambda v: v.get('exchange', v.get('exchange_name')),
        ),
        origins=(
            Origin(OriginSection.POINT_ARGS, 'config'),
        ),
        stage=Stage.INIT,
    ),
    Rule(
        description="Задать имя участку",
        destination=Destination(
            DestinationSection.SPAN_NAME,
            'name'
        ),
        pipeline=(
            partial(pipe_sep_string, **{'sep': ("::", " (", ")")}),
        ),
        origins=(
            Origin(
                OriginSection.ENGINE,
                ext_api_kind,
            ),
            Origin(
                OriginSection.REUSE,
                "peer_name",
            ),
            Origin(
                OriginSection.CALL_STACK,
                ext_tracer_out_point,
            ),
        ),
        stage=Stage.INIT,
    ),
    Rule(
        description="Наименование партнерского сервиса записать в участок",
        destination=Destination(
            DestinationSection.SPAN_NAME,
            'remote_endpoint',
          ),
        pipeline=(
            pipe_head,
        ),
        origins=(
            Origin(OriginSection.REUSE, 'peer_name'),
        ),
        stage=Stage.PRE,
    ),
    Rule(
        description="Путь по методам, вызвавшим запрос",
        destination=Destination(DestinationSection.SPAN_TAGS, 'query'),
        pipeline=(
            pipe_head,
        ),
        origins=(
            Origin(OriginSection.CALL_STACK, ext_tracer_path),
        ),
        stage=Stage.INIT,
    ),
    Rule(
        description="Вывести праметры SQL запроса в аннотации",
        destination=Destination(DestinationSection.SPAN_LOGS, 'message'),
        pipeline=(
            pipe_head,
            pipe_catch_essential,
            PipeCommand.TEE,
            Destination(DestinationSection.SPAN_TAGS, {}),
            pipe_dump,
            pipe_cut,
            pipe_mask_secret,
        ),
        origins=(
            Origin(
                OriginSection.POINT_ARGS,
                'message',
            ),
        ),
        stage=Stage.PRE,
    ),
    Rule(
        description="Запомнить ошибку для вывода",
        destination=Destination(DestinationSection.REUSE, 'error'),
        pipeline=(
            pipe_head,
        ),
        origins=(
            Origin(OriginSection.SPAN, 'error'),
        ),
        stage=Stage.POST,
    ),
)
