from django.apps import AppConfig


class CareersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dropsride.careers"

    def ready(self):
        try:
            import dropsride.careers.signals  # noqa F401
        except ImportError:
            pass
