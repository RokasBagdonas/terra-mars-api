from django.urls import include, path
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"players", views.PlayerViewSet)
router.register(r"games", views.GameViewSet)
router.register(r"player_games", views.PlayerGameViewSet)

urlpatterns = [path("", include(router.urls))]
