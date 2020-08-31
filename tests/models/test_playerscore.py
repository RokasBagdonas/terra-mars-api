import pytest
from django.db.utils import IntegrityError

from mars_api.models import Game, Player, PlayerScore

from ..factories import GameFactory, PlayerScoreFactory

pytestmark = pytest.mark.django_db


def test_can_create_multiple_player_scores_same_player(player, player_score_factory):
    ps1 = player_score_factory(player=player)
    ps2 = player_score_factory(player=player)

    assert PlayerScore.objects.filter(player=player).count() == 2



def test_player_not_allowed_to_have_multiple_scores_in_the_same_game(game, player_score_factory):
    """
    Tests if only unique players can be added to the PlayerScore with same game_id.
    (So that there wouldn't be a player that has two scores for the same Game.)
    """
    ps1 = player_score_factory(game=game)
    with pytest.raises(IntegrityError):
        ps2 = player_score_factory(corporation="Terractor", player=ps1.player, game=game)


def test_same_player_in_different_games(player, player_score_factory):
    """
    Tests if a Player is allowed to have multiple scores but in different games.
    Tested by not throwing an exception on the second PlayerScore creation.
    """
    ps1 = player_score_factory(player=player)
    ps2 = player_score_factory(player=player)

    assert ps1.player.nickname == ps2.player.nickname
    assert ps1.game != ps2.game


def test_cannot_create_player_score_with_invalid_corporation():
    with pytest.raises(IntegrityError):
        PlayerScoreFactory(corporation="")


def test_cannot_have_duplicate_corporations_same_game(game, player_score_factory):
    ps1 = player_score_factory(game=game)

    with pytest.raises(IntegrityError):
        player_score_factory(game=game)


def test_can_have_same_corporation_same_player_different_games(player, game_factory, player_score_factory):
    """Prerequisite: PLayerScoreFactory'ies use the same corporation."""
    corporation = "Thorgate"
    g1 = game_factory()
    ps1 = player_score_factory(game=g1, corporation=corporation, player=player)

    g2 = game_factory()
    ps2 = player_score_factory(game=g2, corporation=corporation, player=player)
