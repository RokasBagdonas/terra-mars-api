import pytest

from mars_api.models import Game, Player, PlayerScore

pytestmark = pytest.mark.django_db


def test_unique_players_for_the_same_game(saved_game, saved_player, unsaved_playerscore):
    """
    Tests if only unique players can be added to the PlayerScore with same game_id.
    (So that there wouldn't be a player that has two scores for the same Game.)
    """

    # 1. mock Game and Player
    g = saved_game
    p = saved_player
    # 2. create two PlayerScore objects with same Game and Player.
    ps1 = unsaved_playerscore(
            game=g,
            player=p
        )

    # ps2 = 


    # 3. when saving a second one, an exception should be thrown.
    # example: "one player cannot have two scores in the same game."

    pytest.fail("unimplemented")


def test_cannot_create_player_score_with_invalid_corporation():

    pytest.fail("unimplemented")
