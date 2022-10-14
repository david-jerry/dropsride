from django.db.models import Q, Manager, Count, Max, Avg
from django.db.models.query import QuerySet


class RidersQueryset(QuerySet):
    """Return most used querysets for drivers

    Args:
        QuerySet (_type_): _description_
    """

    def verified(self):
        return self.filter(approved=True)

    def counts(self):
        return self.verified().count()

class RidersManager(Manager):
    def get_queryset(self):
        return RidersQueryset(self.model, using=self._db)

    def verified(self):
        return self.get_queryset().verified()

    def counts(self):
        return self.get_queryset().counts()

