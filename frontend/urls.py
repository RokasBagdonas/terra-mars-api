from django.urls import path

from frontend.views import IndexView

urlpatterns = [
    path("", IndexView.as_view()),
    path("games/", IndexView.as_view()),
]
