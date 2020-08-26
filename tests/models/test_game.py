import pytest

from mars_api.models import MAPS, Game

pytestmark = pytest.mark.django_db


def test_game_and_player_scores_create_success(api_client):
    """Tests if a new Game and new PlayerScores can be created in one POST.
       Also ensures that new Players can be created.
    """
    # 1. prep data

    # 2. request

    # 3. check response

    # 4. check db


def test_game_cannot_be_created_with_invalid_game_map():
    pytest.skip("unimplemented")


def test_game_returns_players_nicknames():
    """When PlayerScores exist, check that corresponding Player nicknames are returned."""

    # 1. Create PlayerScores. Sidenote: PlayerScores should be allowed to be created without an existing Player.

    # 2. GET a Game

    # 3. assert if nicknames exist in game.players property.
