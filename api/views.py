from api.models import Game, Player, PlayerScore
from api.serializers import GameSerializer, PlayerScoreSerializer, PlayerSerializer
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class PlayerScoreViewSet(viewsets.ModelViewSet):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
