import pytest
from pytest_factoryboy import register

from .factories import (
    GameDictFactory,
    GameFactory,
    PlayerDictFactory,
    PlayerFactory,
    PlayerScoreDictFactory,
    PlayerScoreFactory,
)

register(PlayerFactory)
register(GameFactory)
register(PlayerScoreFactory)

register(PlayerDictFactory)
register(GameDictFactory)
register(PlayerScoreDictFactory)


@pytest.fixture()
def api_client():
    from rest_framework.test import APIClient

    return APIClient()
