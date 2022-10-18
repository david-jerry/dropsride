from django.db.models import Q, Manager, Count, Max, Avg
from django.db.models.query import QuerySet

class CareersQueryset(QuerySet):
    """Return most used querysets for posts

    Args:
        QuerySet (_type_): _description_
    """

    def published(self):
        return self.filter(draft=False).order_by("-published_date")

    def search(self, query):
        qs = self
        if query is not None:
            lookup = (
                Q(title__icontains=query) |
                Q(content__icontains=query)
            )
            qs = qs.published().filter(lookup).distinct()
        return qs

    def get_recent_careers(self):
        try:
            return self.published()[:12]
        except IndexError:
            return None


class CareersManager(Manager):
    def get_queryset(self):
        return CareersQueryset(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query):
        return self.get_queryset().search(query)

    def get_recent_careers(self):
        return self.get_queryset().get_recent_careers()


