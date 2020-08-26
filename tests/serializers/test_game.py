import pytest

from mars_api.serializers import GameAndPlayersScoresSerializer

from ..factories import PlayerScoreFactory


def test_game_and_players_scores_serializer():
    # 1. need dict data for player scores, and game.
    ps1 = {"corporation": "Thorgate", "player": {"nickname": "A"}}
    ps2 = {"corporation": "Tharsis Republic", "player": {"nickname": "B"}}

    game = {"game_map": "Elysium"}
    data = {"players_scores": [ps1, ps2], "game": game}
    serializer = GameAndPlayersScoresSerializer(data=data)

    assert serializer.is_valid()
