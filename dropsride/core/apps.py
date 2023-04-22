from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoresConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dropsride.core"
    verbose_name = _("Core Views")
