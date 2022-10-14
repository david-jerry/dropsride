from django.urls import path

from .views import (
    news_list_view,
    tagged_post,
)

app_name = "news"
urlpatterns = [
    path("", view=news_list_view, name="list"),
    path("tagged/<slug>/", view=tagged_post, name="tag"),
    # path("category/<slug>/", view=categorized_posts, name="category"),
    # path("<slug>/", view=post_detail_view, name="detail"),
    # path("<slug>/update", view=post_update_view, name="update"),
]
