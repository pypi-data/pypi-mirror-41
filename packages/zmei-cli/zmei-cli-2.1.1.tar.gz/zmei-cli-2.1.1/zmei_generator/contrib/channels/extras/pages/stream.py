import re

from zmei_generator.domain.application_def import ApplicationDef
from zmei_generator.domain.extras import PageExtra
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class StreamModel(object):

    def __init__(self, page) -> None:
        self.page = page
        self.target = None
        self.filter_expr = None
        self.fields = None

    @property
    def class_name(self):
        return self.target

    @property
    def stream_name(self):
        return re.sub('[^a-z0-9]+', '_', self.target.lower())


class StreamPageExtra(PageExtra):
    # stream

    def __init__(self, page) -> None:
        super().__init__(page)

        self.models = []

    def get_required_apps(self):
        return ['django_query_signals']

    def get_required_deps(self):
        return ['django-query-signals']


class StreamPageExtraParserListener(BaseListener):

    def __init__(self, application: ApplicationDef) -> None:
        super().__init__(application)

        self.stream_model = None

    def enterAn_stream(self, ctx: ZmeiLangParser.An_streamContext):
        stream = StreamPageExtra(self.page)
        self.application.extras.append(
            stream
        )

        self.page.application.channels = True
        self.page.stream = stream

    def enterAn_stream_target_model(self, ctx: ZmeiLangParser.An_stream_target_modelContext):
        super().enterAn_stream_target_model(ctx)

        stream_model = StreamModel(self.page)
        target = ctx.getText()

        if target.startswith('#'):
            model = self.application.resolve_model(target[1:])
            stream_model.target = model.class_name
            self.page.imports.append((f'{model.application.app_name}.models', model.class_name))
        else:
            stream_model.target = target

        self.page.stream.models.append(
            stream_model
        )

        self.stream_model = stream_model

    def enterAn_stream_target_filter(self, ctx: ZmeiLangParser.An_stream_target_filterContext):
        self.stream_model.filter_expr = self._get_code(ctx)

    def enterAn_stream_field_name(self, ctx: ZmeiLangParser.An_stream_field_nameContext):
        field_name = ctx.getText()

        if not self.stream_model.fields:
            self.stream_model.fields = [field_name]
        else:
            self.stream_model.fields.append(field_name)
