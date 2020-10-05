import pytest
from rest_framework import status

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
