import factory

faker = factory.Faker


class PlayerFactory(factory.django.DjangoModelFactory):

    nickname = faker("name")
    motto = "mottos can be the same"

    class Meta:
        model = "mars_api.Player"


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "mars_api.Game"


class PlayerScoreFactory(factory.django.DjangoModelFactory):

    player = factory.SubFactory(PlayerFactory)
    game = factory.SubFactory(GameFactory)

    class Meta:
        model = "mars_api.PlayerScore"
