from django.urls import include, path

from frontend.views import IndexView


urlpatterns = [path("", IndexView.as_view()), ]
