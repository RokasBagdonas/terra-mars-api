from contextlib import ExitStack as does_not_raise
import pytest
from django.db.utils import IntegrityError

from mars_api.models import PlayerScore

pytestmark = pytest.mark.django_db


def test_can_create_multiple_player_scores_same_player(player, player_score_factory):
    player_score_factory.create_batch(player=player, size=2)

    assert PlayerScore.objects.filter(player=player).count() == 2


def test_player_not_allowed_to_have_multiple_scores_in_the_same_game(
    game, player_score_factory
):
    """
    Tests if only unique players can be added to the PlayerScore with same game_id.
    (So that there wouldn't be a player that had two scores for the same Game.)
    """
    ps1 = player_score_factory(game=game)
    with pytest.raises(IntegrityError):
        player_score_factory(corporation="Terractor", player=ps1.player, game=game)


def test_same_player_in_different_games(player, player_score_factory):
    """
    Tests if a Player is allowed to have multiple scores but in different games.
    Tested by not throwing an exception when second PlayerScore is created.
    """
    ps1 = player_score_factory(player=player)
    ps2 = player_score_factory(player=player)
    with does_not_raise():
        assert ps1.player.nickname == ps2.player.nickname
        assert ps1.game != ps2.game


def test_cannot_create_player_score_with_invalid_corporation(player_score_factory):
    with pytest.raises(IntegrityError):
        player_score_factory(corporation="")


def test_to_str_num_queries(django_assert_num_queries, player_score):
    with django_assert_num_queries(0):
        print(str(player_score))
