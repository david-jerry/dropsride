from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from dropsride.transactions.models import Transaction
from dropsride.utils.logger import LOGGER


class TransactionSerializer(serializers.ModelSerializer):
    content_object = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = [
            "content_object",
            "content_type",
            "object_id",
            "slug",
            "amount",
            "transaction_reason",
            "transaction_status",
            "ref_code",
            "url",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:transaction-detail", "lookup_field": "slug"}
        }

    def get_content_object(self, obj):
        content_type = ContentType.objects.get_for_id(obj.content_type.id)
        model_class = content_type.model_class()
        serializer_class = self.context.get("serializers", {}).get(
            content_type.model, None
        )
        if serializer_class:
            serializer = serializer_class(
                model_class.objects.get(pk=obj.object_id), context=self.context
            )
            return serializer.data
        return None

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["owner"] = instance.owner.username
        return ret

    def update(self, instance, validated_data):
        # Ensure the user cannot update the `user`
        validated_data.pop("owner", None)
        return super().update(instance, validated_data)
