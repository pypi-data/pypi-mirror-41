from collections import namedtuple
from zmei_generator.generator.imports import ImportSet
from zmei_generator.parser.errors import GlobalScopeValidationError as ValidationException


class ApplicationDef(object):
    # app_name: str
    # models: Dict[str, ModelDef]

    def __init__(self, app_name: str) -> None:

        # self.parser = parser
        self.application = None

        self.app_name = app_name

        self.translatable = False

        #
        # TODO: move platform-specific fields out of definition
        #

        self.theme = None
        self.theme_install = False

        self.api = False
        self.rest = False
        self.docker = False
        self.celery = False
        self.gitlab = False
        self.channels = False
        self.crud = False
        self.suit = False
        self.filer = False
        self.langs = False
        self.admin = False
        self.react = False
        self.flutter = False
        self.models = {}
        self.pages = {}
        self.react_deps = {}
        self.react_imports = ImportSet()
        self.page_imports = ImportSet()
        self.model_imports = ImportSet()

        self.deps = []
        self._apps = [app_name]
        self.extras = []

        self.files = {}
        
    def resolve_page(self, page_name_def):
        if '.' in page_name_def:
            if not self.application:
                raise ValidationException(
                    'Application have no application assigned. Can not resolve reference.')

            app_name, page_name = page_name_def.split('.', maxsplit=2)

            if app_name not in self.application.applications:
                raise ValidationException(
                    f'Unknown application: {app_name}, when trying to resolve model name "{page_name_def}". '
                    f'Available apps are: {",".join(self.application.applications)}')

            return self.application.applications[app_name].pages[page_name]
        else:
            return self.pages[page_name_def]

    def resolve_model(self, model_name_def):
        try:
            if '.' in model_name_def:
                if not self.application:
                    raise ValidationException(
                        'Application have no application assigned. Can not resolve reference.')

                app_name, model_name = model_name_def.split('.', maxsplit=2)

                if app_name not in self.application.applications:
                    raise ValidationException(
                        f'Unknown application: {app_name}, when trying to resolve model name "{model_name_def}". '
                        f'Available apps are: {",".join(self.application.applications)}')

                return self.application.applications[app_name].models[
                    model_name]
            else:
                return self.models[model_name_def]
        except KeyError:
            raise ValidationException('Reference to unknown model: #{}'.format(model_name_def))
        

    def add_deps(self, deps):
        for dep in deps:
            if dep not in self.deps:
                self.deps.append(dep)

    def add_apps(self, apps):
        for app in apps:
            if app not in self._apps:
                self._apps.append(app)

    @property
    def has_sitemap(self):
        for key, page in self.pages.items():
            if page.has_sitemap:
                return True

        return False

    @property
    def apps(self):
        app_names = self._apps
        return app_names

    def page_list(self):
        return list(self.pages.values())

    def post_process(self):
        for col in self.models.values():
            col.post_process()

    def post_process_extras(self):
        for extra in self.extras:
            extra.post_process()

    def get_required_apps(self):
        all_apps = []
        for col in self.models.values():
            all_apps.extend(col.get_required_apps())

        for extra in self.extras:
            all_apps.extend(extra.get_required_apps())

        return list(set(all_apps))

    def get_required_deps(self):
        all_deps = []
        for col in self.models.values():
            all_deps.extend(col.get_required_deps())

        for extra in self.extras:
            all_deps.extend(extra.get_required_deps())
        return list(set(all_deps))

    def get_required_urls(self):
        all_urls = []
        for col in self.models.values():
            all_urls.extend(col.get_required_urls())

        for extra in self.extras:
            all_urls.extend(extra.get_required_urls())
        return all_urls

    def get_required_settings(self):
        all_settings = {}
        for col in self.models.values():
            all_settings.update(col.get_required_settings())

        for extra in self.extras:
            all_settings.update(extra.get_required_settings())
        return all_settings


FieldDeclaration = namedtuple('FieldDeclaration', ['import_def', 'declaration'])


