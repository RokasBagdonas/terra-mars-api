from rest_framework import viewsets

from mars_api.models import Game, Player, PlayerScore
from mars_api.serializers import GameSerializer, PlayerScoreSerializer, PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class PlayerScoreViewSet(viewsets.ModelViewSet):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer


"""
Game Scores viewset that:
1. Returns a game and corresponding PlayerScores.
2. Posts a game with PlayerScores.
"""

