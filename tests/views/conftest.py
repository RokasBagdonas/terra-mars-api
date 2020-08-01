import pytest

from mars_api.models import Player


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def saved_player():
    p = Player.objects.create(nickname="my nickname", motto="a short phrase")
    return p

@pytest.fixture
def unsaved_player():
    p = Player(nickname="unsaved player nickname", motto="usaved player phrase")
    return p
