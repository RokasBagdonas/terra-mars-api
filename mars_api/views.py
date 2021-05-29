from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, viewsets

from mars_api.filters import GameFilter, PlayerScoreFilter
from mars_api.models import Game, Player, PlayerScore, CORPORATIONS, MAPS
from mars_api.serializers import (
    GameAndPlayersScoresSerializer,
    GamePlayerCountSerializer,
    PlayerScoreSerializer,
    PlayerSerializer,
)


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


from rest_framework.decorators import api_view
from django.http import HttpResponse

def public(request):
    return HttpResponse("You don't need to be authenticated to see this")

@api_view(['GET'])
def private(request):
    return HttpResponse("Private Auth0 message!")
