from api.models import Game, PlayerGame, Player
from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class PlayerGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerGame
        fields = "__all__"
