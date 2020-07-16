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

    # post game scores
    # when detail=True, DefaultRouter will add pk to the url
    @action(detail=False, methods=["post"])
    def game(self, request, format=None):
        """
        TODO test cases:
        0. does save_player_games add game_id to each player_score
        1. will game be deleted if save_player_games throws an error?
        2. match number_of_players vs number_of_scores
        3. invalid data for game
        4. invalid data for player_score(s)
        """

        def save_player_games(players_scores_data, game_id):
            players_scores_serializer = PlayerScoreSerializer(
                data=players_scores_data, many=True, context={"game_id": game_id}
            )

            try:
                if players_scores_serializer.is_valid():
                    players_scores_serializer.save()
            except ValidationError:
                return Response(
                    players_scores_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )

        # 1. save Game
        game_serializer = GameSerializer(data=request.data["Game"])

        if game_serializer.is_valid():
            try:
                # save game here because game_id is required for adding player_scores
                game_id = game_serializer.save().id
                number_of_players = game_serializer.number_of_players
                # 2. validate and save each player score
                players_scores_data = request.data["PlayersScores"]

                number_of_scores = len(players_scores_data)
                if (
                    number_of_players != number_of_scores
                    or number_of_scores < 1
                    or number_of_scores > 5
                ):
                    return Response(
                        "too many/few player game scores {number_of_scores} or Game.number_of_players does not match the number of scores",
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                save_player_games(players_scores_data, game_id, number_of_players)

            except ValidationError:
                Game.objects.get(pk=game_id).delete()

            return Response(game_serializer.data, status=status.HTTP_201_CREATED)

        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Get all player scores

    # def player(self, request):
    # pass

    # # get all scores from a game
    # @action(detail=False)
    # def game(self, request):
    #     pass
