import pytest
from django.db.utils import IntegrityError

from mars_api.models import MAPS, Game

from ..factories import PlayerScoreFactory

pytestmark = pytest.mark.django_db


def test_game_cannot_be_created_with_invalid_game_map():

    with pytest.raises(IntegrityError):
        Game.objects.create(game_map="Invalid name")


def test_game_can_be_created_with_valid_game_map():
    Game.objects.create(game_map="Tharsis")


def test_game_returns_related_players_scores(game):
    """When PlayerScores exist, check that corresponding Player nicknames are returned."""

    ps1 = PlayerScoreFactory(game=game)
    ps2 = PlayerScoreFactory(game=game)

    assert game.players_scores.count() == 2

