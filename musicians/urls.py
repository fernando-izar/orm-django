from django.urls import path
from .views import MusicianView

urlpatterns = [
    path("musicians/", MusicianView.as_view()),
]
