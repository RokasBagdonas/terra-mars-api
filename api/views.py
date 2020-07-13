from api.models import Game, Player, PlayerGame
from api.serializers import GameSerializer, PlayerGameSerializer, PlayerSerializer
from django.shortcuts import render
from rest_framework import viewsets


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlayerGameViewSet(viewsets.ModelViewSet):
    queryset = PlayerGame.objects.all()
    serializer_class = PlayerGameSerializer
