from contextlib import ExitStack as does_not_raise
import pytest

from mars_api.models import PlayerScore
from mars_api.serializers import PlayerScoreForGameSerializer, PlayerScoreSerializer

pytestmark = pytest.mark.django_db


def test_playerscore_serializes_player(game):
    ps = {"corporation": "Thorgate", "player": {"nickname": "Petras"}, "game": game.id}

    serializer = PlayerScoreSerializer(data=ps)

    assert serializer.is_valid()


def test_playerscore_for_game():
    """Tests if a player score can be created without a game when using PlayerScoreForGameSerializer"""

    ps = {"corporation": "Thorgate", "player": {"nickname": "John"}}

    serializer = PlayerScoreForGameSerializer(data=ps)
    assert serializer.is_valid()


def test_same_player_multiple_scores(player, game_factory):
    """Tests if `get_or_create` properly functions when calling PlayerScoreSerializer."""
    g = game_factory()
    data = {
        "corporation": "Thorgate",
        "player": {"nickname": player.nickname},
        "game": g.id,
    }
    ps_serializer = PlayerScoreSerializer(data=data)
    assert ps_serializer.is_valid()
    ps_serializer.save()

    g = game_factory()
    data["game"] = g.id
    ps_serializer = PlayerScoreSerializer(data=data)

    assert ps_serializer.is_valid()
    ps_serializer.save()
    with does_not_raise():
        PlayerScore.objects.get(game=g.id)
    assert PlayerScore.objects.filter(player=player).count() == 2
