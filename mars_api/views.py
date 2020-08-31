from rest_framework import viewsets

from mars_api.models import Game, Player, PlayerScore
from mars_api.serializers import (
    GameAndPlayersScoresSerializer,
    GameSerializer,
    PlayerScoreSerializer,
    PlayerSerializer,
)


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class PlayerScoreViewSet(viewsets.ModelViewSet):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer


class GameScoresViewSet(viewsets.ModelViewSet):
    """A viewset for Game and related PlayerScores."""

    queryset = Game.objects.all()
    serializer_class = GameAndPlayersScoresSerializer
