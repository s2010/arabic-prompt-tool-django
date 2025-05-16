# prompts/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # Route WebSocket connections starting with ws://.../ws/prompts/ to PromptConsumer
    re_path(r'ws/prompts/$', consumers.PromptConsumer.as_asgi()),
]
