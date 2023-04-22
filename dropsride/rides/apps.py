from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RidesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dropsride.rides"
    verbose_name = _("Rides")

    def ready(self):
        try:
            import dropsride.rides.signals  # noqa F401
        except ImportError:
            pass
