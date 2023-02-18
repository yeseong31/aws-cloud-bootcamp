from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from chat.views import base_views

app_name = 'chat'

urlpatterns = [
    # 홈페이지
    path('home/', base_views.home, name='home'),
    # 방 생성 및 입장 (SocketIO)
    path('', base_views.enter_room, name='enter_room'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
