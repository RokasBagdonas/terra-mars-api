import pytest

from mars_api.models import Game, Player, PlayerScore

pytestmark = pytest.mark.django_db


def test_unique_players_for_the_same_game():
    """
    Tests if only unique players can be added to the PlayerScore with same game_id.
    (So that there wouldn't be a player that has two scores for the same Game.)
    """

    # 1. create Game and Player

    # 2. create two PlayerScore objects with same Game and Player.

    # ps2 =

    # 3. when saving a second one, an exception should be thrown.
    # example: "one player cannot have two scores in the same game."

    pytest.skip("unimplemented")


def test_cannot_create_player_score_with_invalid_corporation():

    pytest.skip("unimplemented")


def test_cannot_have_duplicate_corporations_same_game():

    pytest.skip("unimplemented")


def test_player_score_without_player(player_score):
    """ Tests if a PlayerScore can be created without existing Player model,
        but with a provided Player nickname. """

    # 1. remove Player

    pytest.skip("unimplemented")

