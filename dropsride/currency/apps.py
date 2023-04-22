from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CurrencyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dropsride.currency"
    verbose_name = _("Currencies")

    def ready(self):
        try:
            import dropsride.currency.signals  # noqa F401
        except ImportError:
            pass
