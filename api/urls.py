from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from api.views import notion_views

app_name = 'api'

urlpatterns = [
    # Notion API
    path('notion/add/', notion_views.notion_database_view, name='notion_database_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
