from django.core.cache import cache
from django.db import models
from django.db.models import Count, Q


class CareersQueryset(models.QuerySet):
    def published(self):
        return self.filter(draft=False).order_by("-published_date")

    def search(self, query):
        if query:
            return self.filter(
                Q(title__icontains=query)
                | Q(team__title__icontains=query)
                | Q(location__state__state__iexact=query)
                | Q(content__icontains=query)
            ).distinct()
        return self.none()


class CareersManager(models.Manager):
    def get_queryset(self):
        return CareersQueryset(self.model, using=self._db).prefetch_related(
            "team", "location"
        )

    def published_careers(self):
        return self.get_queryset().published()

    def search_published_careers(self, query):
        if query == "all":
            return self.published_careers()

        cache_key = f"search_careers_{query}"
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = self.published_careers().search(query)
            cache.set(cache_key, queryset, timeout=1 * 60 * 60)
        return queryset

    def all_published_careers(self):
        cache_key = "all_published_careers"
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = self.published_careers()
            cache.set(cache_key, queryset)
        return queryset

    def get_recent_careers(self, num_posts=10):
        cache_key = f"recent_published_careers{num_posts}"
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = (
                self.all_published_careers()
                .annotate(num_applications=Count("applications"))
                .order_by("-published_date", "-num_applications")[:num_posts]
            )
            cache.set(cache_key, queryset, timeout=1 * 60 * 60)
        return queryset

    def all_careers(self):
        cache_key = "all_careers"
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = self.get_queryset().all()
            cache.set(cache_key, queryset)
        return queryset

    def search_careers(self, query):
        if query == "all":
            return self.all_careers()

        cache_key = f"search_careers_{query}"
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = self.get_queryset().search(query)
            cache.set(cache_key, queryset, timeout=1 * 60 * 60)
        return queryset
