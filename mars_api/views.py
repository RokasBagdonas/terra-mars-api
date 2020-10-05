from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from rest_framework import filters, viewsets

from mars_api.models import Game, Player, PlayerScore
from mars_api.serializers import (GamePlayerCountSerializer, GameSerializer,
                                  PlayerScoreSerializer, PlayerSerializer,
                                  GameAndPlayersScoresSerializer)


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GameViewSet(viewsets.ModelViewSet):
    # queryset = Game.objects.all()
    # serializer_class = GameSerializer
    queryset = Game.objects.annotate(player_count=Count("scores"))
    serializer_class = GamePlayerCountSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        "date",
        "game_map",
        "number_of_generations",
        "draft_variant",
        "prelude",
        "venus_next",
        "colonies",
    ]


class PlayerScoreViewSet(viewsets.ModelViewSet):
    queryset = PlayerScore.objects.prefetch_related("player", "game")
    serializer_class = PlayerScoreSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["player", "corporation"]


class GameScoresViewSet(viewsets.ModelViewSet):
    """A viewset for Game and related PlayerScores."""

    queryset = Game.objects.prefetch_related("scores", "scores__player")
    serializer_class = GameAndPlayersScoresSerializer
