# from braces.views import CsrfExemptMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from taggit.models import Tag

from config.pagination import CustomPagination
from dropsride.blog.api.serializers import NewsSerializer, TagSerializer
from dropsride.blog.models import News


class TagViewset(
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    lookup_field = "slug"
    permission_classes = [AllowAny]
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return self.queryset
        return []


class NewsViewset(
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    """Blog posts endpoint. When adding the tags they should look like thsi

    {
        'title': "name of the post title",
        'content': "the content of the post",
        'tags': ["tags1", "tags2", "tags3"]
    }

    Args:
        ListModelMixin (GET): Gets the list of blog posts created
        RetrieveModelMixin (GET): Returns a single blog post instance
        UpdateModelMixin (PUT): Updates a single blog post by its slug name
        CreateModelMixin (POST): Creates a new blog post and auto matically creates the slug field from teh backend
        DestroyModelMixin (DELETE): Deletes a single post item from teh backend with only staff permission

    Returns:
        _type_: _description_
    """

    serializer_class = NewsSerializer
    queryset = News.published.all_published_posts()
    lookup_field = "slug"
    permission_classes = [AllowAny]
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return self.queryset
        return News.published.all_posts()
