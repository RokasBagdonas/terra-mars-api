"""A module for testing player model."""
import pytest
from django.contrib.auth.models import User

from mars_api.models import Player

pytestmark = pytest.mark.django_db


def test_player_is_created():
    """Test if Player and User is created."""
    user = User.objects.create_user("my_username", "email@email.it", "password")
    player = Player(user=user, nickname="my_nickname", motto="short motto")
    user.save()
    player.save()

    db_user = User.objects.get(username="my_username")
    db_player = User.objects.select_related("player").first().player

    assert db_user.username == "my_username"
    assert db_user.email == "email@email.it"
    assert db_player.nickname == "my_nickname"
    assert db_player.motto == "short motto"
