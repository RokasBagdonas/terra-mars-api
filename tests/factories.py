import factory

faker = factory.Faker


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
    game_map = "Tharsis"
    draft_variant = False
    prelude = False
    venus_next = False


class PlayerScoreFactory(factory.django.DjangoModelFactory):
    player = factory.SubFactory(PlayerFactory)
    game = factory.SubFactory(GameFactory)
    corporation = "Thorgate"

    class Meta:
        model = "mars_api.PlayerScore"


class PlayerScoreDictFactory(factory.DictFactory):
    corporation = "Thorgate"
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
