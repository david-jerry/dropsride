from django.db.models import Q, Manager, Count, Max, Avg
from django.db.models.query import QuerySet

class NewsQueryset(QuerySet):
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

    def get_popular_posts(self):
        try:
            return self.published().order_by("-hit_count_generic__hits")[1:12]
        except IndexError:
            return None

    def get_recent_posts(self):
        try:
            return self.published()[:12]
        except IndexError:
            return None

    def featured_post(self):
        try:
            return self.published().filter(featured=True).first()
        except IndexError:
            return None


class NewsManager(Manager):
    def get_queryset(self):
        return NewsQueryset(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query):
        return self.get_queryset().search(query)

    def get_popular_posts(self):
        return self.get_queryset().get_popular_posts()

    def get_recent_posts(self):
        return self.get_queryset().get_recent_posts()

    def get_featured_post(self):
        return self.get_queryset().featured_post()


