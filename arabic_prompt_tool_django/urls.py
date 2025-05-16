# arabic_prompt_tool_django/urls.py
from django.contrib import admin
from django.urls import path, include
# Remove the import of api_app and any custom asgi handlers
# from api import api_app
# async def api_asgi_handler(...): ...
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prompts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Remove the line mounting the FastAPI app via Django's URLconf:
    # re_path(r'^api/', api_asgi_handler),
    # or re_path(r'^api/', api_app),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
