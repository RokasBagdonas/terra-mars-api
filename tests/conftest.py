import pytest
from django.utils import timezone
from pytest_factoryboy import register

from .factories import PlayerFactory
from mars_api.models import Game, Player, PlayerScore

register(PlayerFactory)


@pytest.fixture
def saved_game():
    g = Game.objects.create(date=timezone.now(), game_map="Tharsis")
    return g
