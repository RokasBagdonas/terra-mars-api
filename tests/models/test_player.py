"""A module for testing player model."""
import pytest
from django.contrib.auth.models import User

from mars_api.models import Player

pytestmark = pytest.mark.django_db


def test_player_is_created():
    """Tests if Player and User are created."""
    user = User.objects.create_user("my_username", "email@email.it", "password")
    player = Player(user=user, nickname="my_nickname", motto="short motto")
    user.save()
    player.save()

    db_player = Player.objects.get(nickname=player.nickname)

    assert db_player.nickname == "my_nickname"
    assert db_player.motto == "short motto"
    assert db_player.user is not None
