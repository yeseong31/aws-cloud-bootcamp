from django.urls import path

from chat.views import test_views

app_name = 'chat'

urlpatterns = [
    # ----- Test -----
    path('test/', test_views.test, name='test'),
    
]
