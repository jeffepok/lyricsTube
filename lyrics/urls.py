from django.urls import path
from .models import Song
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]