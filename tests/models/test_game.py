from datetime import datetime

import pytest
from mars_api.models import Game


@pytest.mark.django_db
def test_game_is_created():
    game = Game(date=datetime.today(), game_map="THR")
    game.save()
    db_game = Game.objects.first()

    assert isinstance(db_game, Game)
