from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, min_length=8)
    company = serializers.CharField(max_length=500, min_length=5)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15, min_length=11)
    message = serializers.CharField()
