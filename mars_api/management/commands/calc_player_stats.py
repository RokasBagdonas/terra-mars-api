from django.core.management.base import BaseCommand

from mars_api.tasks import calc_all_player_stats


class Command(BaseCommand):
    help = "Calculates all players' statistics"

    def handle(self, *args, **options):
        calc_all_player_stats()
