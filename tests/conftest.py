from pytest_factoryboy import register

from .factories import GameFactory, PlayerFactory, PlayerScoreFactory

register(PlayerFactory)
register(GameFactory)
register(PlayerScoreFactory)
