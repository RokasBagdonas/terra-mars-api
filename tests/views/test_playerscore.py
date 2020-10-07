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


def test_can_filter_by_milestones(api_client, player_score_factory):
    milestones_score = 5
    player_score_factory.create_batch(1, milestones=milestones_score)
    player_score_factory.create_batch(2, milestones=10)

    params = {"milestones": 5}
    response = api_client.get(PLAYERSCORE_PATH, params)

    assert response.status_code == status.HTTP_200_OK

    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["milestones"] == milestones_score


def test_can_filter_by_player_nickname(api_client, player_factory, player_score_factory):
    num_of_scores = 2
    p1 = player_factory.create()
    p2 = player_factory.create()
    player_score_factory.create_batch(num_of_scores, player=p1)
    # arbitrary player to check that query does not return all scores
    player_score_factory.create_batch(1, player=p2)

    params = {"player__nickname": p1.nickname}
    response = api_client.get(PLAYERSCORE_PATH, params)

    assert response.status_code == status.HTTP_200_OK

    assert len(response.data["results"]) == num_of_scores
    assert response.data["results"][0]["player"]["nickname"] == p1.nickname
