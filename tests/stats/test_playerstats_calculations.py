from decimal import Decimal

import pytest

from mars_api.models import Player, PlayerScore, PlayerStats
from mars_api.stats import playerstats_calculations as psc

pytestmark = pytest.mark.django_db


def test_get_games_played_none(player):
    assert 0 == psc.get_games_played(player.id)


def test_get_games_played_multiple(player, player_score_factory):
    player_score_factory.create_batch(player=player, size=2)
    assert 2 == psc.get_games_played(player.id)


def test_player_win_percentage_none(player):
    assert None == psc.get_player_win_percentage(player.id)


def test_player_win_percentage_real_number(player, player_score_factory):
    player_score_factory.create_batch(player=player, size=2, is_winner=False)
    player_score_factory.create(player=player, is_winner=True)
    games_played = 3
    assert round(Decimal(0.33), 2) == round(
        Decimal(psc.get_player_win_percentage(player.id, games_played)), 2
    )


def test_get_most_popular_corporation_none(player, player_score_factory):
    assert None == psc.get_most_popular_corporation(player.id)


def test_get_most_popular_corporation_one_top(player, player_score_factory):
    player_score_factory.create_batch(player=player, size=4, corporation="Inventrix")
    player_score_factory.create_batch(player=player, size=3, corporation="Teractor")
    res = psc.get_most_popular_corporation(player.id)
    print(res)
    assert "Inventrix" == res[0]
