# Create your tasks here

from celery import shared_task
from mars_api.models import Player


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_players():
    count = Player.objects.count()
    print("=== counted players: " + count)
    return Player.objects.count()


@shared_task
def rename_player_nickname(player_id, name):
    p = Player.objects.get(id=player_id)
    p.nickname = name
    p.save()
