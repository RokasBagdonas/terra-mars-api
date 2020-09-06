import pytest
from django.db.utils import IntegrityError

from mars_api.models import Game

pytestmark = pytest.mark.django_db


def test_game_cannot_be_created_with_invalid_game_map():
    with pytest.raises(IntegrityError):
        Game.objects.create(game_map="Invalid name")


def test_game_can_be_created_with_valid_game_map():
    Game.objects.create(game_map="Tharsis")


def test_game_returns_related_players_scores(game, player_score_factory):
    """When PlayerScores exist, check that corresponding Player nicknames are returned."""

    player_score_factory(game=game)
    player_score_factory(game=game, corporation="Terractor")

    assert game.players_scores.count() == 2


def test_cannot_have_duplicate_corporations_same_game(game, player_score_factory):
    player_score_factory(game=game)

    with pytest.raises(IntegrityError):
        player_score_factory(game=game)  # same corporations when using 🏭


def test_can_have_same_corporation_same_player_different_games(
    player, game_factory, player_score_factory
):
    """Prerequisite: PLayerScoreFactory'ies use the same corporation."""
    corporation = "Thorgate"
    g1 = game_factory()
    player_score_factory(game=g1, corporation=corporation, player=player)

    g2 = game_factory()
    player_score_factory(game=g2, corporation=corporation, player=player)
