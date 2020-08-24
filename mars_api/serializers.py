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


class PlayerSerializerForScore(PlayerSerializer):
    """
       The difference between the default `PlayerSerializer` is that this one negates the
       `unique` constraint of the nickname. This is because when creating a PlayerScore,
        we want to have the option to create a Player if one doesn't exist.
    """

    nickname = serializers.CharField(max_length=32)

    def create(self, validated_data):
        instance, _ = Player.objects.get_or_create(**validated_data)
        return instance


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
    game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all(), allow_null=True)

    def create(self, validated_data):
        player_data = validated_data.pop("player")
        player, _ = Player.objects.get_or_create(**player_data)

        player_score = PlayerScore.objects.create(player=player, **validated_data)
        return player_score

    class Meta:
        model = PlayerScore
        fields = "__all__"


class GameAndPlayersScoresSerializer(serializers.ModelSerializer):
    """
    Serializes a Game as well as PlayerScores.
    """

    players_scores = PlayerScoreForGameSerializer(many=True)

    class Meta:
        model = Game
        fields = [
            "date", "game_map", "draft_variant",
            "prelude", "venus_next",
            "colonies", "players_scores",
        ]

    def create(self, validated_data):
        """
        Issue 1: game has to be created before validating player scores.
        However, the `PlayerScoreSerializer` is using the default `PlayerScore` model that requires Game.

        Solutions:
        1. Alter/Create PlayerScoreSerializer that does not have not null FK constraint so
        that validation passes. Once validation passes, add the same game instance to each
        PlayerScore and then save it to db.
        """
        # 1. create a game
        players_scores = validated_data.pop("players_scores")

        game = Game.objects.create(**validated_data)

        # 2. create player_scores
        players_scores_instances = []
        for ps in players_scores:
            players_scores_instances.append(PlayerScore.objects.create(**ps))

        # 3. return
        result = {"game": game, "players_scores": players_scores_instances}
        return result
