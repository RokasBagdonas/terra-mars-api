from rest_framework import serializers

from mars_api.models import Game, Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
