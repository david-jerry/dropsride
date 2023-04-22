from django.db.models import Q
from rest_framework import status
# from braces.views import CsrfExemptMixin
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from config.pagination import CustomPagination
from dropsride.settings.api.serializers import CartypeSerializer, LocalizationSerializer
from dropsride.settings.models import CarType, Localization


class LocalizationViewset(
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = LocalizationSerializer
    queryset = Localization.objects.all()
    lookup_field = "uuid"
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            return self.queryset
        return None


class CartypeViewset(
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = CartypeSerializer
    queryset = CarType.objects.all()
    lookup_field = "slug"
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
