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


class PlayerSerializerForScore(serializers.ModelSerializer):
    """
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
    player = PlayerSerializerForScore()

    def create(self, validated_data):
        player_data = validated_data.pop("player")
        player, _ = Player.objects.get_or_create(**player_data)

        player_score = PlayerScore.objects.create(player=player, **validated_data)
        return player_score

    class Meta:
        model = PlayerScore
        fields = "__all__"


class PlayerScoreForGameSerializer(serializers.ModelSerializer):
    player = PlayerSerializerForScore()

    def create(self, validated_data):
        player_data = validated_data.pop("player")
        player, _ = Player.objects.get_or_create(**player_data)

        player_score = PlayerScore.objects.create(player=player, **validated_data)
        return player_score

    class Meta:
        model = PlayerScore
        exclude = ["game"]


class GameAndPlayersScoresSerializer(serializers.ModelSerializer):
    """
    Serializes a Game as well as PlayerScores.
    """

    players_scores = PlayerScoreForGameSerializer(many=True)

    class Meta:
        model = Game
        fields = "__all__"

    def create(self, validated_data):
        # 1. create a game
        players_scores = validated_data.pop("players_scores")
        game = Game.objects.create(**validated_data)

        # 2. create player_scores
        players_scores_instances = []
        for ps in players_scores:
            p, _ = Player.objects.get_or_create(**ps.pop("player"))
            players_scores_instances.append(
                PlayerScore.objects.create(player=p, game=game, **ps)
            )

        result = {"game": game, "players_scores": players_scores_instances}
        return result
