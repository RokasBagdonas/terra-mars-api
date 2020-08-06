import factory

faker = factory.Faker


class PlayerFactory(factory.django.DjangoModelFactory):

    nickname = faker('name')
    motto = "mottos can be the same"

    class Meta:
        model = "mars_api.Player"
