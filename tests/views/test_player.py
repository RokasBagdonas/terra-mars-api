import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from api.models import Player
from api.views import PlayerViewSet

pytestmark = pytest.mark.django_db

BASE_PATH = "/api/players/"


def mock_player(nickname, motto=""):
    p = Player(nickname=nickname, motto=motto)
    p = p.save()
    return Player.objects.get(nickname=nickname)


def get_url_with_id(id):
    return BASE_PATH + str(id) + "/"


def test_can_get_player_data(api_client):
    """Tests if client can receive player JSON data."""
    # 1. create a player in the database
    data = {"nickname": "my_nickname", "motto": "short phrase"}
    p = mock_player(data["nickname"], data["motto"])
    id = p.id

    url = get_url_with_id(id)
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data["nickname"] == p.nickname
    assert response.data["motto"] == p.motto


def test_create_player_without_user(api_client):
    """Tests if it's possible to create a player without user."""
    data = {"nickname": "nicky nick"}

    response = api_client.post(BASE_PATH, data)
    assert response.status_code == 201

    p = Player.objects.get(nickname=data["nickname"])
    assert isinstance(p, Player)
    assert p.nickname == data["nickname"]


def test_delete_player(api_client):
    """Tests if a player can be deleted provided their nickname."""
    data = {"nickname": "three", "motto": ""}

    p = mock_player(data["nickname"], data["motto"])

    response = api_client.delete(get_url_with_id(p.id))

    assert response.status_code == 204
    with pytest.raises(Player.DoesNotExist):
        Player.objects.get(nickname=data["nickname"])
