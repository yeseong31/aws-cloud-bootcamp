from django.urls import path

from chat.views import base_views

app_name = 'chat'

urlpatterns = [
    # 홈페이지
    path('home/', base_views.home, name='home'),
    # 방 생성 및 입장 (SocketIO)
    # path('room/', base_views.create_room, name='create_room'),
    path('', base_views.enter_room, name='enter_room'),
]
