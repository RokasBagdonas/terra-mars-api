import factory
# PR: what if I just use factory.Faker(provider_str) instead of importing this?
# "how to Use [Faker] with Factory Boy": https://faker.readthedocs.io/en/latest/
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class PlayerFactory(factory.django.DjangoModelFactory):

    nickname = factory.Faker('name')
    motto = "mottos can be the same"

    class Meta:
        model = "mars_api.Player"
