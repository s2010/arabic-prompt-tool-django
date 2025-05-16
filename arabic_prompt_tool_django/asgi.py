# arabic_prompt_tool_django/asgi.py
import os

from django.core.asgi import get_asgi_application

# Set the Django settings module first
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arabic_prompt_tool_django.settings') # <-- Verify your project name here

# Get Django's ASGI application. This initializes the app registry.
django_asgi_app = get_asgi_application()

# Import Channels routing and Starlette/FastAPI after Django's app registry is ready
from channels.routing import ProtocolTypeRouter, URLRouter # Import ProtocolTypeRouter and URLRouter
from starlette.routing import Mount
from starlette.applications import Starlette
from api import api_app
from prompts import routing # Import your app's routing

# Define the main ASGI application using ProtocolTypeRouter
# This routes requests based on protocol type (http, websocket, etc.)
application = ProtocolTypeRouter({
    "http": Starlette(routes=[ # Handle HTTP requests using Starlette router
        Mount('/api', app=api_app), # FastAPI routes
        Mount('/', app=django_asgi_app), # Django HTTP routes
    ]),
    "websocket": URLRouter(routing.websocket_urlpatterns), # Handle WebSocket requests using Channels URLRouter
    # You can add other protocols like "channel" here if needed
})
