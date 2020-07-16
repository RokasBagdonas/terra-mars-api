from api.models import Game, Player, PlayerScore
from api.serializers import GameSerializer, PlayerScoreSerializer, PlayerSerializer
from django.shortcuts import render
from rest_framework import status, viewsets
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


class GameScores(APIView):
    """ a class for POST'ing a Game and a PlayerGames (scores) 
        1. validate game.
        1.1 if valid, create it and get its id
        2. for each player_game, append gameId
        2.1 validate player_games
        2.2 if any fail, remove created game from database

    """

    def post(self, request, format=None):
        def save_player_games(players_scores_data, game_id):
            players_scores_serializer = PlayerScoreSerializer(
                players_scores_data, many=True
            )

            for player_game in players_scores_serializer:
                player_game["game_id"] = game_id
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

                # 2. validate and save each player score
                players_scores_data = request.data["PlayersScores"]

                number_of_scores = len(players_scores_data)
                if number_of_scores < 1 or number_of_scores > 5:
                    return Response(
                        "too many/few player game scores {number_of_scores}",
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                save_player_games(players_scores_data, game_id)

            # TODO testing: will the game be deleted if save_player_games throws an error?
            except ValidationError:
                Game.objects.get(pk=game_id).delete()

            return Response(game_serializer.data, status=status.HTTP_201_CREATED)

        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
