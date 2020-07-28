import pytest
from rest_framework import status

from mars_api.models import Player

pytestmark = pytest.mark.django_db

PLAYER_PATH = "/mars_api/players/"


def get_url_with_id(id):
    return PLAYER_PATH + str(id) + "/"


def test_can_get_player_data(api_client, saved_player):
    """Tests if client can receive player JSON data."""
    id = saved_player.id

    response = api_client.get(get_url_with_id(id))

    assert response.status_code == status.HTTP_200_OK
    assert response.data
    assert response.data["nickname"] == saved_player.nickname
    assert response.data["motto"] == saved_player.motto


def test_create_player_without_user(api_client):
    """Tests if it's possible to create a player without user."""
    data = {"nickname": "nicky nick"}

    response = api_client.post(PLAYER_PATH, data)
    assert response.status_code == status.HTTP_201_CREATED

    response_data = response.data
    # check if db actually generated an id.
    assert isinstance(response_data["id"], int)
    assert response_data["nickname"] == data["nickname"]


def test_delete_player(api_client, saved_player):
    """Tests if a player can be deleted provided their nickname."""
    response = api_client.delete(get_url_with_id(saved_player.id))

    assert response.status_code == status.HTTP_204_NO_CONTENT
    with pytest.raises(Player.DoesNotExist):
        Player.objects.get(nickname=saved_player.nickname)


def test_fail_change_to_duplicate_nickname(api_client, unsaved_player):
    """Tests if only unique player nicknames are allowed."""
    unsaved_player.nickname = "nickname1"
    unsaved_player.save()
    player2 = Player.objects.create(nickname="nick2", motto="")
    data = {"nickname": unsaved_player.nickname}

    endpoint = get_url_with_id(player2.id)
    response = api_client.patch(endpoint, data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert isinstance(Player.objects.get(nickname=player2.nickname), Player)


def test_change_player_nickname(api_client, saved_player):
    """Tests if player nickname can be changed."""
    data = {"nickname": "new nickname"}

    endpoint = get_url_with_id(saved_player.id)
    response = api_client.patch(endpoint, data)
    assert response.status_code == status.HTTP_200_OK

    db_player = Player.objects.get(nickname="new nickname")
    assert saved_player.id == db_player.id
