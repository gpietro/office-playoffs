from django.apps import AppConfig


class WebappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webapp'

    def ready(self):
        from django.contrib.auth.signals import user_logged_in
        from .signals import create_player

        user_logged_in.connect(create_player, sender=self)
