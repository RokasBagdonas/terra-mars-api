import pytest
from pytest_factoryboy import register

from .factories import GameFactory, PlayerFactory, PlayerScoreFactory
from .factories.dictionaries import (
    PlayerDictFactory,
    PlayerScoreDictFactory,
    GameDictFactory,
)

register(PlayerFactory)
register(GameFactory)
register(PlayerScoreFactory)

register(PlayerDictFactory)
register(GameDictFactory)
register(PlayerScoreDictFactory)


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()
