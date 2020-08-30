import pytest
from django.db.utils import IntegrityError

from mars_api.models import Game, Player, PlayerScore

from ..factories import PlayerScoreFactory

pytestmark = pytest.mark.django_db


def test_unique_players_for_the_same_game(game):
    """
    Tests if only unique players can be added to the PlayerScore with same game_id.
    (So that there wouldn't be a player that has two scores for the same Game.)
    """
    ps1 = PlayerScoreFactory(game=game)
    with pytest.raises(IntegrityError):
        ps2 = PlayerScoreFactory(corporation="Terractor", player=ps1.player, game=game)


def test_cannot_create_player_score_with_invalid_corporation():
    with pytest.raises(IntegrityError):
        PlayerScoreFactory(corporation="")


def test_cannot_have_duplicate_corporations_same_game(game):
    ps1 = PlayerScoreFactory(game=game)

def test_cannot_have_duplicate_corporations_same_game():

    pytest.skip("unimplemented")


def test_player_score_without_player(player_score):
    """ Tests if a PlayerScore can be created without existing Player model,
        but with a provided Player nickname. """

    # 1. remove Player
    pytest.skip("unimplemented")
