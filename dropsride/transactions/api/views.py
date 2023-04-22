from django.core.cache import cache
from django.db.models import Q
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    """Transaction endpoint is automatically created when a user performs certain post request to make payments on line

    Args:
        RetrieveModelMixin (GET): Get a specific transaction by its slug (a unique query parameter like this: https://dropsride.com/link-to-the-transaction/slug-parameter/)
        ListModelMixin (GET): Get all transaction if you are the super admin or else only transactions for a certain user

    Returns:
        JSON: A json response of all transactions by a user permission type or a single transaction detail
    """

    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        user = self.request.user
        if user.is_staff:
            cache_key = "all_transactions"
            queryset = cache.get(cache_key)
            if queryset is None:
                queryset = self.queryset
                cache.set(cache_key, queryset)
        else:
            cache_key = f"transactions_{user.id}"
            queryset = cache.get(cache_key)
            if queryset is None:
                queryset = self.queryset.filter(owner__id=self.request.user.id)
                cache.set(cache_key, queryset)
        return queryset

    # custom action to retrieve the currenctly signed in users transactions
    @action(
        detail=False,
        methods=["GET"],
        permission_classes=[IsAuthenticated],
        url_path="my-transactions",
    )
    def my_transactions(self, request):
        transactions = self.queryset.filter(owner=request.user)
        if transactions:
            serializer = self.get_serializer(transactions, many=True)
            return Response(serializer.data)
        return Response({"message": "No transactions found."}, status=404)
