import pytest
from api.models import Player
from django.contrib.auth.models import User

pytestmark = pytest.mark.django_db

def test_user_is_created():
    """
    tests if User is created.
    """
    user = User.objects.create_user("my_username", "email@email.it", "password")
    user.save()

    db_user = User.objects.get(username="my_username")

    assert db_user.username == "my_username" and db_user.email == "email@email.it"

def test_player_is_created():
    """
    Test if Player is created alongisde the User.
    """

    user = User.objects.create_user("my_username", "email@email.it", "password")
    user.save()

    db_player = User.objects.select_related("player").first().player

    assert isinstance(db_player, Player)
