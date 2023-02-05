from django.urls import path

from chat.views import sio_views

app_name = 'chat'

urlpatterns = [
    # ----- SocketIO -----
    path('', sio_views.chat, name='chat'),
    
]
