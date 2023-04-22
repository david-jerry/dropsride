from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TicketsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dropsride.tickets"
    verbose_name = _("Tickets")

    def ready(self):
        try:
            import dropsride.tickets.signals  # noqa F401
        except ImportError:
            pass
