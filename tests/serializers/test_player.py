"""A module for testing player serializer."""
import pytest
from django.contrib.auth.models import User

from api.models import Player
from api.serializers import PlayerSerializer

pytestmark = pytest.mark.django_db


def test_player_serializer():
    """Check if Json object including User produces two """
    player_data = {"nickname": "my_nickname", "motto": "a brief phrase"}

    player_object = Player(nickname=player_data["nickname"], motto=player_data["motto"])
    player_serializer = PlayerSerializer(data=player_data)

    assert player_serializer.is_valid()
    assert player_serializer.data["nickname"] == player_object.nickname
    assert player_serializer.data["motto"] == player_object.motto
