from django.urls import include, path
from rest_framework import routers

from mars_api import views

router = routers.DefaultRouter()
router.register(r"players", views.PlayerViewSet)
router.register(r"games", views.GameViewSet, basename="games")
router.register(r"player_scores", views.PlayerScoreViewSet)
router.register(r"game_scores", views.GameScoresViewSet)
router.register(r"player_stats", views.PlayerStatsViewSet)

urlpatterns = [
    path("corporations", views.ListCorporations.as_view()),
    path("maps", views.ListMaps.as_view()),
    path("", include(router.urls)),
    path("public", views.public),
    path("private", views.private),
    path("count_players", views.count_players),
    path("player_stats/calc", views.calc_player_stats),
]
