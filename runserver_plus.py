from django_extensions.management.commands.runserver_plus import (
    Command as RunServerCommand,
)


class Command(RunServerCommand):
    def get_options(self, *args, **kwargs):
        options = super().get_options(*args, **kwargs)
        options["ssl_cert"] = "cert.pem"
        options["ssl_key"] = "key.pem"
        return options
