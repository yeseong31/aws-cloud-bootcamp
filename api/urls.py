from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from api.views import notion_views

app_name = 'api'

urlpatterns = [
    # Notion API
    path('notion/add/', notion_views.add_item_to_database, name='add_item_to_database'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
