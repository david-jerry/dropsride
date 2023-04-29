from datetime import date

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
from dropsride.settings.api.serializers import (
    CartypeSerializer,
    LocalizationSerializer,
    PromoSerializer,
    PromoSubscribersSerializer,
)
from dropsride.settings.models import CarType, Localization, Promo, PromoUsage


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


class PromoViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    @action(
        detail=True,
        methods=["GET"],
        permission_classes=[IsAuthenticated],
        url_path="promo-subscribe",
    )
    def subscribe_to_promo(self, request, *args, **kwargs):
        """enpoint to get subscribe to a promo

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        user = request.user
        promo = self.get_object()
        PromoUsage.obects.get_or_create(
            promo=promo,
            subscriber=user,
            used=True,
            used_date=date.today(),
        )
        serializer = PromoSerializer(promo, context={"request", request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class PromoSubscriberViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = PromoUsage.objects.all()
    serializer_class = PromoSubscribersSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
