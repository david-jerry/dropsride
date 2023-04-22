# from django.urls import path

# websocket_urlpatterns = [
#     # path('ws/user/<str:username>/', UserConsumer.as_asgi()),
#     # path('ws/chat/<int:room_id>/', ChatConsumer.as_asgi()),
# ]


async def websocket_application(scope, receive, send):
    while True:
        event = await receive()

        if event["type"] == "websocket.connect":
            await send({"type": "websocket.accept"})

        if event["type"] == "websocket.disconnect":
            break

        if event["type"] == "websocket.receive":
            if event["text"] == "ping":
                await send({"type": "websocket.send", "text": "pong!"})
