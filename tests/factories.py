from datetime import datetime
import random

import factory
from mars_api.models import CORPORATIONS
from faker.providers import BaseProvider

faker = factory.Faker


class CorporationProvider(BaseProvider):
    def corporation(self):
        return random.choice(list(CORPORATIONS))[0]


faker.add_provider(CorporationProvider)

class PlayerFactory(factory.django.DjangoModelFactory):
    nickname = factory.Faker("name")
    motto = ""

    class Meta:
        model = "mars_api.Player"


class PlayerDictFactory(factory.DictFactory):
    nickname = faker("name")
    motto = ""


class GameFactory(factory.django.DjangoModelFactory):
    game_map = "Tharsis"

    class Meta:
        model = "mars_api.Game"


class GameDictFactory(factory.DictFactory):
    player_scores = []  # to be added
    number_of_generations = 10
    date = datetime.now()
    game_map = "Tharsis"
    draft_variant = False
    prelude = False
    colonies = False
    venus_next = False


class PlayerScoreFactory(factory.django.DjangoModelFactory):
    player = factory.SubFactory(PlayerFactory)
    game = factory.SubFactory(GameFactory)
    corporation = faker("corporation")

    class Meta:
        model = "mars_api.PlayerScore"


class PlayerScoreDictFactory(factory.DictFactory):
    corporation = "Thorgate"
    player = factory.SubFactory(PlayerDictFactory)
    game = 0  # to be set
    terraform_rating = 0
    milestones = 0
    awards = 0
    greeneries = 0
    cities = 0
    event_cards = 0
    automated_cards = 0
    active_cards = 0
    resources = 0
    is_winner = False
