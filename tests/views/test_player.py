import pytest
from rest_framework import status

from ..factories import PlayerFactory
from mars_api.models import Player

pytestmark = pytest.mark.django_db

PLAYER_PATH = "/mars_api/players/"


def get_url_with_id(id):
    return PLAYER_PATH + str(id) + "/"


def test_can_get_player_data(api_client, player):
    """Tests if client can receive player JSON data."""
    id = player.id

    response = api_client.get(get_url_with_id(id))

    assert response.status_code == status.HTTP_200_OK
    assert response.data
    assert response.data["nickname"] == player.nickname
    assert response.data["motto"] == player.motto


def test_create_player_without_user(api_client):
    """Tests if it's possible to create a player without user."""
    data = {"nickname": "nicky nick"}

    response = api_client.post(PLAYER_PATH, data)
    assert response.status_code == status.HTTP_201_CREATED

    response_data = response.data
    # check if db actually generated an id.
    assert isinstance(response_data["id"], int)
    assert response_data["nickname"] == data["nickname"]


def test_delete_player(api_client, player):
    """Tests if a player can be deleted provided their nickname."""
    response = api_client.delete(get_url_with_id(player.id))

    assert response.status_code == status.HTTP_204_NO_CONTENT
    with pytest.raises(Player.DoesNotExist):
        Player.objects.get(nickname=player.nickname)


def test_fail_change_to_duplicate_nickname(api_client):
    """Tests if only unique player nicknames are allowed."""
    p1 = PlayerFactory()
    p2 = PlayerFactory()
    data = {"nickname": p1.nickname}

    endpoint = get_url_with_id(p2.id)
    response = api_client.patch(endpoint, data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert isinstance(Player.objects.get(nickname=p2.nickname), Player)


def test_change_player_nickname(api_client, player):
    """Tests if player nickname can be changed."""
    data = {"nickname": "new nickname"}

    endpoint = get_url_with_id(player.id)
    response = api_client.patch(endpoint, data)
    assert response.status_code == status.HTTP_200_OK

    db_player = Player.objects.get(nickname="new nickname")
    assert player.id == db_player.id
