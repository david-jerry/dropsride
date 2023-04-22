from django.contrib import admin

# Register your models here.
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "publisher",
        "published_date",
        "tag_list",
        "created",
        "modified",
    ]
    list_editable = ["author", "publisher"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())


admin.site.register(News, NewsAdmin)
