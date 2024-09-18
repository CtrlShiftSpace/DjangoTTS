from django.urls import path

from . import views

urlpatterns = [
    path('edge/tts', views.edge_tts, name="edge_tts"),
]