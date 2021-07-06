from django.db.models import Count
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from mars import celery
from mars_api import tasks
from mars_api.filters import GameFilter, PlayerScoreFilter
from mars_api.models import CORPORATIONS, MAPS, Game, Player, PlayerScore, PlayerStats
from mars_api.serializers import (
    GameAndPlayersScoresSerializer,
    GamePlayerCountSerializer,
    PlayerScoreSerializer,
    PlayerSerializer,
    PlayerStatsSerializer,
)
from rest_framework import filters, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.annotate(player_count=Count("scores"))
    serializer_class = GamePlayerCountSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = GameFilter


class PlayerScoreViewSet(viewsets.ModelViewSet):
    queryset = PlayerScore.objects.prefetch_related("player", "game")
    serializer_class = PlayerScoreSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = PlayerScoreFilter


class PlayerStatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlayerStats.objects.all()
    serializer_class = PlayerStatsSerializer


class GameScoresViewSet(viewsets.ModelViewSet):
    """A viewset for Game and related PlayerScores."""

    queryset = Game.objects.prefetch_related("scores", "scores__player")
    serializer_class = GameAndPlayersScoresSerializer


class ListCorporations(APIView):
    def get(self, request):
        return Response([name for (name, *_) in CORPORATIONS])


class ListMaps(APIView):
    def get(self, request):
        return Response([name for (name, *_) in MAPS])


def public(request):
    return HttpResponse("You don't need to be authenticated to see this")


@api_view(["GET"])
def private(request):
    return HttpResponse("Private Auth0 message!")


def count_players(request):
    celery.debug_task()
    tasks.count_players.delay()
    return HttpResponse("Counting players... ")
