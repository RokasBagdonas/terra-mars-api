import factory

from mars_api.models import MAPS

faker = factory.Faker


class PlayerDictFactory(factory.DictFactory):
    nickname = faker("name")
    motto = ""


class PlayerScoreDictFactory(factory.DictFactory):
    corporation = ""  # to be set
    player = factory.SubFactory(PlayerDictFactory)
    game = ""  # to be set
    terraform_rating = 0
    milestones = 0
    awards = 0
    greeneries = 0
    cities = 0
    event_cards = 0
    automated_cards = 0
    active_cards = 0
    resources = 0


class GameDictFactory(factory.DictFactory):
    player_scores = []  # to be added
    game_map = "Tharsis"
    draft_variant = False
    prelude = False
    venus_next = False

