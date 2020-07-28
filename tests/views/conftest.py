import pytest

from mars_api.models import Player


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def player():
    p = Player.objects.create(nickname="my nickname", motto="a short phrase")
    return p
