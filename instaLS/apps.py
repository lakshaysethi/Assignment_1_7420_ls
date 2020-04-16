from django.apps import AppConfig


class InstalsConfig(AppConfig):
    name = 'instaLS'

    def ready(self):
        import instaLS.signals