from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TransactionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dropsride.transactions"
    verbose_name = _("Transactions")

    def ready(self):
        try:
            import dropsride.transactions.signals  # noqa F401
        except ImportError:
            pass
