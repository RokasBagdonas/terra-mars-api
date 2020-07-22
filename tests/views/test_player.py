import pytest

from api.models import Player

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


def test_fail_change_to_duplicate_nickname(api_client):
    """Tests if player nickname is not allowed to be changed to an already existing one."""
    p1 = mock_player("nick1", "")
    p2 = mock_player("nick2", "")
    data = {"nickname": p1.nickname}

    url = get_url_with_id(p2.id)
    response = api_client.put(url, data)

    assert response.status_code == 400
    assert p2.nickname == Player.objects.get(nickname=p2.nickname).nickname


def test_change_player_nickname(api_client):
    """Test if it player nickname can be changed."""
    p = mock_player("nick1")
    data = {"nickname": "new nickname"}

    url = get_url_with_id(p.id)
    response = api_client.put(url, data)
    assert response.status_code == 200
    assert p.id == Player.objects.get(nickname=data["nickname"]).id
