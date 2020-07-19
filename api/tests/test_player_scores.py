import pytest
from api.models import Game, PlayerScore
from rest_framework.test import APIRequestFactory
from api.views import PlayerScoreViewSet
from rest_framework import status

pytestmark = pytest.mark.django_db
