import pytest

from mars_api.views import GameViewSet

GAME_PATH = "mars_api/games/"

pytestmark = pytest.mark.django_db


def test_can_post_game_with_player_scores():
    """Test if a game can be created alongside PlayerScores in one POST."""
    # 1. Mock a Game and PlayerScores

    # 2. POST it

    # 3. check if successful

    # 4. check if exists in db

    pytest.fail("unimplemented")
