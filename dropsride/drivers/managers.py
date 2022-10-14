from django.db.models import Q, Manager, Count, Max, Avg
from django.db.models.query import QuerySet


class DriversQueryset(QuerySet):
    """Return most used querysets for drivers

    Args:
        QuerySet (_type_): _description_
    """

    def verified(self):
        return self.filter(is_blocked=False)

    def banned(self):
        return self.filter(is_blocked=True)

class DriversManager(Manager):
    def get_queryset(self):
        return DriversQueryset(self.model, using=self._db)

    def verified(self):
        return self.get_queryset().verified()

    def banned(self):
        return self.get_queryset().banned()

