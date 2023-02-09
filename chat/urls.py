from django.urls import path

from chat.views import base_views

app_name = 'chat'

urlpatterns = [
    # 홈페이지
    path('', base_views.home, name='home'),
    # 방 생성
    path('room/create/', base_views.create_room, name='create_room'),
    # 방 입장 (SocketIO)
    path('chat/<str:room_code>/', base_views.chat, name='chat'),
]
