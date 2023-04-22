from django.core.cache import cache
from django.db.models import Avg, Count, Manager, Max, Q
from django.db.models.query import QuerySet


class NewsQueryset(QuerySet):
    def published(self):
        return self.filter(draft=False).order_by("-published_date")

    def search(self, query):
        if query:
            lookup = (
                Q(title__icontains=query)
                | Q(summary__icontains=query)
                | Q(keywords__icontains=query)
                | Q(content__icontains=query)
            )
            return self.filter(lookup)
        return self.none()


class NewsManager(Manager):
    def get_queryset(self):
        return NewsQueryset(self.model, using=self._db).prefetch_related("author")

    def get_related_posts(self, news, num_related_posts=3):
        """
        Returns a queryset of `num_related_posts` News objects that are related to the given `news` object,
        based on shared tags.
        """
        cache_key = f"related_news_{news.id}"
        queryset = cache.get(cache_key)
        if queryset is None:
            tags = news.tags.all()
            if not tags:
                return self.none()
            related_posts = (
                self.filter(Q(tags__in=tags) & ~Q(id=news.id))
                .published()
                .distinct()[:num_related_posts]
            )
            queryset = related_posts
            cache.set(cache_key, queryset)
        return queryset

    def get_featured_posts(self, num_posts=3):
        """
        Returns a queryset of up to `num_posts` featured News objects, ordered by published_date.
        """
        cache_key = "featured_news"
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = self.get_queryset().published().filter(featured=True)[:num_posts]
            cache.set(cache_key, queryset)
        return queryset

    def search_published_posts(self, query):
        """
        Returns a queryset of published News objects that match the given `query` in either the title or content,
        ordered by relevance.
        """
        if query == "all":
            return self.all_published_posts()

        cache_key = f"search_news_{query}"
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = self.get_queryset().published().search(query)
            cache.set(cache_key, queryset)
        return queryset

    def all_published_posts(self):
        """
        Returns a queryset of all published News objects.
        """
        cache_key = "all_published_news"
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = self.get_queryset().published()
            cache.set(cache_key, queryset)
        return queryset

    def get_recent_posts(self, num_posts=10):
        """
        Returns a queryset of the most recent published News objects, ordered by publication date.
        """
        cache_key = f"recent_published_news_{num_posts}"
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = self.all_published_posts()[:num_posts]
            cache.set(cache_key, queryset)
        return queryset

    def search_posts(self, query):
        """
        Returns a queryset of published News objects that match the given `query` in either the title or content,
        ordered by relevance.
        """
        if query == "all":
            return self.all_posts()
        cache_key = f"search_admin_news_{query}"
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = self.get_queryset().search(query)
            cache.set(cache_key, queryset)
        return queryset

    def all_posts(self):
        """
        Returns a queryset of all published News objects.
        """
        cache_key = "all_admin_news"
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = self.get_queryset()
            cache.set(cache_key, queryset)
        return queryset

    def get_recent_admin_posts(self, num_posts=10):
        """
        Returns a queryset of the most recent published News objects, ordered by publication date.
        """
        cache_key = f"recent_admin_news_{num_posts}"
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = self.all_posts()[:num_posts]
            cache.set(cache_key, queryset)
        return queryset
