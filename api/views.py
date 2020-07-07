from api.models import Player
from api.serializers import PlayerSerializer
from django.shortcuts import render
from rest_framework import viewsets


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
