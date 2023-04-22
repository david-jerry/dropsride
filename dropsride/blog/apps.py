from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dropsride.blog"

    def ready(self):
        try:
            import dropsride.blog.signals  # noqa F401
        except ImportError:
            pass
