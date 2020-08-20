from rest_framework import serializers

from mars_api.models import Game, Player, PlayerScore


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class PlayerScoreSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    class Meta:
        model = PlayerScore
        fields = "__all__"

    # How to skip unique "nickname" validation for the player?
    def create(self, validated_data):
        player_data = validated_data.pop("player")
        player = Player.objects.get_or_create(**player_data)[0]

        player_score = PlayerScore.objects.create(player=player, **validated_data)
        return player_score
