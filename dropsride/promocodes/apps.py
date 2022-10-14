from django.apps import AppConfig


class PromocodesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dropsride.promocodes'

    def ready(self):
        try:
            import dropsride.promocodes.signals  # noqa F401
        except ImportError:
            pass
