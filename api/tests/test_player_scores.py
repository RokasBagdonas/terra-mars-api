import pytest
from api.models import Game, PlayerScore
from rest_framework.test import APIRequestFactory
from api.views import PlayerScoreViewSet
from rest_framework import status

pytestmark = pytest.mark.django_db

URL_PREFIX = "/api/player_scores/"
URL_GAME = URL_PREFIX + "game/"


# correct_request_data = {
    # "Game": {"date": "2020-07-15T15:54",
             # "game_map": "THR",
             # "number_of_players": 3},
    # "PlayersScores": [
        # {"player_nickname": "Rokas", "corporation": "CRE"},
        # {"player_nickname": "Bokas", "corporation": "HEL"},
        # {"player_nickname": "Pokas", "corporation": "PBL"}
    # ]
# }

correct_request_data = {
    "Game": {
        "date": "2020-07-14T15:35",
        "game_map": "THR",
        "number_of_players": 3
    },
    "PlayersScores": [{
        "player_nickname": "Rokas",
        "corporation": "THR",
        "terraform_rating": 18,
        "milestones": 5,
        "awards": 2,
        "greeneries": 3,
        "cities": 0,
        "event_cards": -2,
        "automated_cards": 23,
        "active_cards": 3,
        "resources": 6
    }]
}


def test_game_createsGame_with_validPlayerScores():
    factory = APIRequestFactory()
    request = factory.post(URL_GAME, correct_request_data, format="json")

    response = PlayerScoreViewSet.as_view()(request)
    print(response)
    assert response.status_code == status.HTTP_201_CREATED
    
    game = Game.objects.first()
    assert game.id == 1











def game_addsGameIdToAllPlayerScores():
    # 1. create a request
    # 1.1 mock data
    pytest.skip("unfinished")
    request_data = {
        "Game": {"date": "2020-07-15T15:54", "game_map": "THR", "number_of_players": 3},
        "PlayerScores": [
            {"player_nickname": "Rokas", "corporation": "CRE"},
            {"player_nickname": "Bokas", "corporation": "HEL"},
            {"player_nickname": "Pokas", "corporation": "PBL"},
        ],
    }

    # 1.2 send the request
    factory = APIRequestFactory()
    request = factory.post(URL_GAME, request_data, format="json")

    # 2. check database
    # 2.1 get game
    game = Game.objects.get(pk=1)
    # 2.2 get PlayerScores by game_id
