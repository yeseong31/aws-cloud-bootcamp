from django.urls import path

from chat.views import base_views

app_name = 'chat'

urlpatterns = [
    # 홈페이지
    path('', base_views.home, name='home'),
    # 방 생성
    path('room/', base_views.create_room, name='create_room'),
    # 방 입장 (SocketIO)
    path('chat/', base_views.enter_room, name='enter_room'),
]
