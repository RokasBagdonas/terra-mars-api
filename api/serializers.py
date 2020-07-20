from rest_framework import serializers

from api.models import Game, Player, PlayerScore


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
