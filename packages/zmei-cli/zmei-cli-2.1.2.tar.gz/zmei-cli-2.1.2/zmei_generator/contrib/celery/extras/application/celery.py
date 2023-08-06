from zmei_generator.domain.application_extra import ApplicationExtra
from zmei_generator.generator.utils import generate_file
from zmei_generator.parser.gen.ZmeiLangParser import ZmeiLangParser
from zmei_generator.parser.utils import BaseListener


class CeleryAppExtra(ApplicationExtra):
    def get_name(cls):
        return 'celery'

    def get_required_deps(self):
        return [
            'celery',
            'redis'
        ]

    @classmethod
    def generate(cls, apps, target_path):
        generate_file(target_path, 'app/celery.py', template_name='celery.py.tpl')
        generate_file(target_path, 'app/tasks.py', template_name='celery_tasks.py.tpl')
        generate_file(target_path, 'app/__init__.py', template_name='celery_init.py.tpl')

    @classmethod
    def write_settings(cls, apps, f):
        f.write("\n")
        f.write("\nCELERY_BROKER_URL = 'redis://127.0.0.1'")
        f.write("\nCELERY_RESULT_BACKEND = 'redis://127.0.0.1'")


class CeleryAppExtraParserListener(BaseListener):

    def enterAn_celery(self, ctx: ZmeiLangParser.An_celeryContext):
        extra = CeleryAppExtra(self.application)
        self.application.extras.append(
            extra
        )
        self.application.celery = extra
