import factory


class PlayerFactory(factory.django.DjangoModelFactory):

    nickname = factory.Faker("name")
    motto = ""

    class Meta:
        model = "mars_api.Player"


class GameFactory(factory.django.DjangoModelFactory):
    game_map = "Tharsis"
    number_of_generations = 10

    class Meta:
        model = "mars_api.Game"


class PlayerScoreFactory(factory.django.DjangoModelFactory):

    player = factory.SubFactory(PlayerFactory)
    game = factory.SubFactory(GameFactory)
    corporation = "Thorgate"

    class Meta:
        model = "mars_api.PlayerScore"
