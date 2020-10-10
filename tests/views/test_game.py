import pytest
from rest_framework import status
from django.db.utils import IntegrityError

from mars_api.models import Game, Player, PlayerScore

GAME_PATH = "/mars_api/games/"
GAME_SCORES_PATH = "/mars_api/game_scores/"

pytestmark = pytest.mark.django_db


def test_can_post_game_with_player_scores(
    api_client, game_dict_factory, player_score_dict_factory
):
    """Test if PlayerScores can be created alongside Game in one POST."""
    game = game_dict_factory()
    ps1 = player_score_dict_factory()
    ps2 = player_score_dict_factory(corporation="Tharsis Republic")

    request = {"scores": []}
    request["game"] = game
    request["scores"].extend([ps1, ps2])

    response = api_client.post(GAME_SCORES_PATH, data=request, format="json")

    assert response.status_code == status.HTTP_201_CREATED

    assert Game.objects.first() is not None
    assert PlayerScore.objects.count() == len(request["scores"])
    assert Player.objects.count() == len(request["scores"])


def test_game_returns_player_count(api_client, game, player_score_factory):
    """Test if the GameViewSet queryset calculates (and in turn serializes) the
    `player_count` aggregate field."""

    id = game.id
    player_score_factory.create(game=game)
    player_score_factory.create(corporation="Helion", game=game)

    response = api_client.get(GAME_PATH + str(id) + "/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["player_count"] == 2


# TODO: where to put this
def generate_player_scores(number_of_scores_per_game, game_factory, player_score_factory):
    """Helper function creating multiple player_scores.

        number_of_scores_per_game: List[int] how many scores per each game.
    """
    corporations = ["Tharsis Republic", "Thorgate", "Helion", "Teractor", "Mining Guild"]
    for i in number_of_scores_per_game:
        g = game_factory()
        for c in corporations[0:i]:
            player_score_factory.create(corporation=c, game=g)


def test_games_returned_by_number_of_players_desc(api_client, game_factory,
        player_score_factory):
    number_of_players = [3, 4, 2, 3]
    generate_player_scores(number_of_players, game_factory, player_score_factory)

    params = {"ordering": "-player_count"}
    response = api_client.get(GAME_PATH, params)

    assert response.status_code == status.HTTP_200_OK

    assert len(response.data["results"]) == len(number_of_players)
    assert response.data["results"][0]["player_count"] == number_of_players[1]
    assert response.data["results"][len(number_of_players)-1]["player_count"] == number_of_players[2]


def test_cannot_post_two_winner_scores(api_client, game_dict_factory,
        player_score_dict_factory):
    g = game_dict_factory()
    ps1 = player_score_dict_factory(is_winner=True)
    ps2 = player_score_dict_factory(corporation="Teractor", is_winner=True)
    request = {"scores": [ps1, ps2], "game": g}

    pytest.fail("TODO: handle constraint errors to return 4** Response")
    response = api_client.post(GAME_SCORES_PATH, data=request, format="json")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
