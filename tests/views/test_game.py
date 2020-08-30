import pytest
from rest_framework import status

from mars_api.models import Game, Player, PlayerScore
from mars_api.views import GameViewSet

from ..factories import dictionaries as factory_dictionaries

GAME_PATH = "/mars_api/games/"
GAME_SCORES_PATH = "/mars_api/game_scores/"

pytestmark = pytest.mark.django_db


def test_can_post_game_with_player_scores(api_client):
    """Test if PlayerScores can be created alongside Game in one POST."""
    # 1. Prep json data
    game = factory_dictionaries.GameDictFactory()
    ps1 = factory_dictionaries.PlayerScoreDictFactory(corporation="Thorgate")
    ps2 = factory_dictionaries.PlayerScoreDictFactory(corporation="Tharsis Republic")

    request = {"players_scores": []}
    request["game"] = game
    request["players_scores"].extend([ps1, ps2])

    # 2. POST it
    print(request)
    response = api_client.post(GAME_SCORES_PATH, data=request, format="json")

    # 3. check if successful
    assert response.status_code == status.HTTP_201_CREATED

    # 4. check if exists in db
    assert Game.objects.first() is not None
    assert PlayerScore.objects.count() == len(request["players_scores"])
    assert Player.objects.count() == len(request["players_scores"])


def test_game_and_player_scores_create_success(api_client):
    """Tests if a new Game and new PlayerScores can be created in one POST.
       Also ensures that new Players can be created.
    """
    # 1. prep data

    # 2. request

    # 3. check response

    # 4. check db
