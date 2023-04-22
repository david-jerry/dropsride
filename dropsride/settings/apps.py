from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SettingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dropsride.settings"
    verbose_name = _("Settings")

    def ready(self):
        try:
            import dropsride.settings.signals  # noqa F401
        except ImportError:
            pass
