import pytest

from mars_api.models import Player
from mars_api.serializers import PlayerSerializer


@pytest.mark.django_db
def test_player_serializer():
    """Checks if it properly serializes the data identical to Player object."""
    player_data = {"nickname": "my_nickname", "motto": "a brief phrase"}

    player_object = Player(**player_data)
    player_serializer = PlayerSerializer(data=player_data)

    assert player_serializer.is_valid()
    assert player_serializer.data["nickname"] == player_object.nickname
    assert player_serializer.data["motto"] == player_object.motto
