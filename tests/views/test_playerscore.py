import pytest
from rest_framework import status

from mars_api.models import Player

pytestmark = pytest.mark.django_db

PLAYERSCORE_PATH = "/mars_api/player_scores/"


def test_playerscore_post_existing_player(game, player, api_client):
    """Tests if a PlayerScore can be posted when a player already exists in db."""
    ps = {
        "corporation": "Thorgate",
        "player": {"nickname": player.nickname},
        "game": game.id,
    }

    response = api_client.post(PLAYERSCORE_PATH, ps, format="json")
    assert response.status_code == status.HTTP_201_CREATED


def test_playerscore_post_new_player(game, api_client):
    """Tests if a PlayerScore can be posted alongside with a new Player."""

    ps = {
        "corporation": "Thorgate",
        "player": {"nickname": "Oak is a Tree"},
        "game": game.id,
    }

    response = api_client.post(PLAYERSCORE_PATH, ps, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Player.objects.get(nickname=ps["player"]["nickname"]) is not None
