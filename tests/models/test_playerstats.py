from decimal import Decimal

import pytest

from mars_api.models import PlayerStats

pytestmark = pytest.mark.django_db


def test_can_create_playerstat(player_factory):
    p = player_factory()
    ps = PlayerStats(
        player=p,
        games_played=22,
        win_percentage=54.78,
        most_popular_corporation="Teractor",
    )
    ps.save()

    psdb = PlayerStats.objects.get(player=p)
    assert psdb.player.nickname == p.nickname
    assert psdb.win_percentage == pytest.approx(Decimal(ps.win_percentage))
    assert psdb.average_player_number == pytest.approx(Decimal(ps.average_player_number))
