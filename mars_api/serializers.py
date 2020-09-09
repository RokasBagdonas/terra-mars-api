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


class GameSerializerForImportedData(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Game
        fields = "__all__"


class NotUniqConstraintPlayerSerializer(serializers.ModelSerializer):
    """Serializes the Player without checking for the unique nickname constraint.

        The difference between the default `PlayerSerializer` is that this one negates the
       `unique` constraint of the nickname. This is because when creating a PlayerScore,
        we want to have the option to create a Player if one doesn't exist or just get the
        existing one via `get_or_create`.
    """

    nickname = serializers.CharField(max_length=32)

    def create(self, validated_data):
        instance, _ = Player.objects.get_or_create(nickname=validated_data["nickname"])
        return instance

    class Meta:
        model = Player
        fields = ["nickname"]


class PlayerScoreSerializer(serializers.ModelSerializer):
    player = NotUniqConstraintPlayerSerializer()

    def create(self, validated_data):
        player_data = validated_data.pop("player")
        player, _ = Player.objects.get_or_create(**player_data)

        return PlayerScore.objects.create(player=player, **validated_data)

    class Meta:
        model = PlayerScore
        fields = "__all__"


class PlayerScoreForGameSerializer(serializers.ModelSerializer):
    player = NotUniqConstraintPlayerSerializer()

    def create(self, validated_data):
        player_data = validated_data.pop("player")
        player, _ = Player.objects.get_or_create(**player_data)

        return PlayerScore.objects.create(player=player, **validated_data)

    class Meta:
        model = PlayerScore
        exclude = ["game"]


class GameAndPlayersScoresSerializer(serializers.ModelSerializer):
    """Serializes a Game as well as PlayerScores."""

    scores = PlayerScoreForGameSerializer(many=True)

    class Meta:
        model = Game
        fields = "__all__"

    def create(self, validated_data):
        players_scores = validated_data.pop("scores")
        game = Game.objects.create(**validated_data)

        players_scores_instances = []
        for player_score in players_scores:
            player, _ = Player.objects.get_or_create(**player_score.pop("player"))
            players_scores_instances.append(
                PlayerScore.objects.create(player=player, game=game, **player_score)
            )

        return {"game": game, "scores": players_scores_instances}
