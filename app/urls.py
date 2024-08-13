from django.urls import path
from . import views
from .routing import websocket_urlpatterns

urlpatterns = [
    path('', views.index), 
]


