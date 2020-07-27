import pytest

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def player():
    from mars_api.models import Player
    p = Player(nickname="my nickname", motto="a short phrase")
    p.save()
    return Player.objects.get(nickname=p.nickname)
