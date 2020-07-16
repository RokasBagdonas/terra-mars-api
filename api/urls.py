from api import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"players", views.PlayerViewSet)
router.register(r"games", views.GameViewSet)
router.register(r"player_scores", views.PlayerScoreViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(r"game_scores", views.GameScores.as_view()),
]
