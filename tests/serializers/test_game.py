import pytest

from mars_api.serializers import GameAndPlayersScoresSerializer

from ..factories.dictionaries import PlayerScoreDictFactory


def test_game_and_players_scores_serializer(player_score_dict_factory, game_dict_factory):
    ps1 = player_score_dict_factory()
    ps2 = player_score_dict_factory()

    g = game_dict_factory()

    print(str(ps1) + "\n" + str(ps2) + "\n", str(g))
    data = {"players_scores": [ps1, ps2], "game": g}
    serializer = GameAndPlayersScoresSerializer(data=data)

    assert serializer.is_valid()
