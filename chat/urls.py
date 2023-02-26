from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from chat.views import base_views

app_name = 'chat'

urlpatterns = [
    # 홈페이지
    path('', base_views.home, name='home'),
    path('home/', base_views.home, name='home'),
    # 방 생성
    path('room/enter/', base_views.enter_room, name='enter_room'),
    # 방 입장
    path('room/create/', base_views.create_room, name='create_room'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
