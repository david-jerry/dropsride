from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdminsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dropsride.admins'
    verbose_name = _("Administrators")

    def ready(self):
        try:
            import dropsride.admins.signals  # noqa F401
        except ImportError:
            pass
