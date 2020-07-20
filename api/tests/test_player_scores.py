import pytest
from api.models import Game, PlayerScore
from api.views import PlayerScoreViewSet
from rest_framework import status
from rest_framework.test import APIRequestFactory

pytestmark = pytest.mark.django_db
