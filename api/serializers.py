from api.models import Game, Player, PlayerScore
from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class PlayerScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerScore
        fields = "__all__"
