import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import serializers

from dropsride.users.api.serializers import UserSerializer
from dropsride.users.api.views import UserViewSet

User = get_user_model()


class UserConsumer(AsyncWebsocketConsumer):
    group_name = "users"

    async def connect(self):
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get("action")
        user_id = data.get("user_id")

        if action == "update":
            await self.update_user(user_id, data)
        elif action == "delete":
            await self.delete_user(user_id)
        elif action == "retrieve":
            await self.retrieve_user(user_id)

    async def update_user(self, user_id, data):
        try:
            user = UserViewSet.queryset.get(id=user_id)
        except User.DoesNotExist:
            return

        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            await self.notify_users(
                {"type": "update", "user": serializer.data},
                user_id,
            )

    async def delete_user(self, user_id):
        try:
            user = UserViewSet.queryset.get(id=user_id)
        except User.DoesNotExist:
            return

        user.delete()
        await self.notify_users({"type": "delete", "user_id": user_id}, user_id)

    async def retrieve_user(self, user_id):
        try:
            user = UserViewSet.queryset.get(id=user_id)
        except User.DoesNotExist:
            return

        serializer = UserSerializer(user)
        await self.send_data({"type": "retrieve", "user": serializer.data})

    async def notify_users(self, data, user_id=None):
        # Invalidate cache for this user
        cache_key = f"user_{user_id}" if user_id else "all_users"
        cache.delete(cache_key)

        await self.channel_layer.group_send(
            self.group_name, {"type": "send_data", "data": data}
        )

    async def send_data(self, data):
        await self.send(text_data=json.dumps(data, cls=DjangoJSONEncoder))
