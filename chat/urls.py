from django.urls import path

from chat.views import base_views, sio_views

app_name = 'chat'

urlpatterns = [
    # ----- Homepage -----
    path('', base_views.home, name='home'),
    # ----- SocketIO -----
    path('chat/', sio_views.chat, name='chat'),
]
