from django.urls import include, path
from rest_framework import routers

from mars_api import views

router = routers.DefaultRouter()
router.register(r"players", views.PlayerViewSet)
router.register(r"games", views.GameViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
