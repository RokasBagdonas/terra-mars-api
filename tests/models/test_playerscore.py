import pytest
from django.db.utils import IntegrityError

from mars_api.models import Game, Player, PlayerScore

from ..factories import GameFactory, PlayerScoreFactory

pytestmark = pytest.mark.django_db


def test_player_not_allowed_to_have_multiple_scores_in_the_same_game(game):
    """
    Tests if only unique players can be added to the PlayerScore with same game_id.
    (So that there wouldn't be a player that has two scores for the same Game.)
    """
    ps1 = PlayerScoreFactory(game=game)
    with pytest.raises(IntegrityError):
        ps2 = PlayerScoreFactory(corporation="Terractor", player=ps1.player, game=game)


def test_same_player_in_different_games(player):
    """
    Tests if a Player is allowed to have multiple scores but in different games.
    Tested by not throwing an exception on second player_score creation.
    """
    ps1 = PlayerScoreFactory(player=player)
    ps2 = PlayerScoreFactory(player=player)

    assert ps1.player.nickname == ps2.player.nickname
    assert ps1.game != ps2.game


def test_cannot_create_player_score_with_invalid_corporation():
    with pytest.raises(IntegrityError):
        PlayerScoreFactory(corporation="")


def test_cannot_have_duplicate_corporations_same_game(game):
    ps1 = PlayerScoreFactory(game=game)

    with pytest.raises(IntegrityError):
        PlayerScoreFactory(game=game)

def test_can_have_same_corporation_same_player_different_games(player):
    """Prerequisite: PLayerScoreFactory'ies use the same corporation."""
    corporation = "Thorgate"
    g1 = GameFactory()
    ps1 = PlayerScoreFactory(game=g1, corporation=corporation, player=player)

    g2 = GameFactory()
    ps2 = PlayerScoreFactory(game=g2, corporation=corporation, player=player)


def test_player_score_without_player(player_score):
    """ Tests if a PlayerScore can be created without existing Player model,
        but with a provided Player nickname. """

    # 1. remove Player
    pytest.skip("unimplemented")
