from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from config.pagination import CustomPagination
from dropsride.currency.models import Banks, Currency, States

from .serializers import BanksSerializer, CurrencySerializer, StateSerializer


class StatesViewSet(ListModelMixin, GenericViewSet):
    serializer_class = StateSerializer
    queryset = States.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination


class CurrencyViewSet(ListModelMixin, GenericViewSet):
    """Endpoint to list all the available currencies

    Args:
        ListModelMixin (_type_): _description_
        GenericViewSet (_type_): _description_
    """

    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination


class BanksViewSet(
    RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet
):
    """This endpoint only shows the list of nigerian banks for now. As times goes on it can accomodate other banks so the system endsup having its own bank details for all banks in the wolrd

    Args:
        RetrieveModelMixin (_type_): _description_
        ListModelMixin (_type_): _description_
        UpdateModelMixin (_type_): _description_
        GenericViewSet (_type_): _description_
    """

    serializer_class = BanksSerializer
    queryset = Banks.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
