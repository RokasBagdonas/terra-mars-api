import pytest

from mars_api.serializers import PlayerScoreSerializer, PlayerScoreForGameSerializer

pytestmark = pytest.mark.django_db

def test_playerscore_serializes_player(game):
    # 1. player and playerscore dict

    ps = {
        "corporation": "Thorgate",
        "player": {"nickname": "Petras"},
        "game": game.id
    }

    # 3. try serialize
    serializer = PlayerScoreSerializer(data=ps)

    # 4. assert if it's Player and PlayerScore
    assert serializer.is_valid()


def test_playerscore_for_game():
    """Tests if a player score can be created without a game when using PlayerScoreForGameSerializer"""

    ps = {
            "corporation": "Thorgate",
            "player": {"nickname": "John"},
            "game": ""
    }

    serializer = PlayerScoreForGameSerializer(data=ps)
    assert serializer.is_valid()
