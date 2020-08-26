import pytest

from mars_api.views import GameViewSet
from ..factories import dictionaries as factory_dictionaries

GAME_PATH = "mars_api/games/"

pytestmark = pytest.mark.django_db


def test_can_post_game_with_player_scores(api_client):
    """Test if PlayerScores can be created alongside Game in one POST."""
    # 1. Create a Game and PlayerScores
    game = factory_dictionaries.GameDictFactory()
    ps1 = factory_dictionaries.PlayerScoreDictFactory(corporation="Thorgate")
    ps2 = factory_dictionaries.PlayerScoreDictFactory(corporation="Tharsis Republic")

    game["player_scores"].append(ps1)
    game["player_scores"].append(ps2)

    # 2. POST it

    # 3. check if successful

    # 4. check if exists in db

    pytest.skip("unimplemented")
