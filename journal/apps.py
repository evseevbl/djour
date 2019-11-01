from django.apps import AppConfig


class JournalConfig(AppConfig):
    name = 'journal'

    def ready(self):
        print('app started')
        # todo константы
        pass
        # startup code here
