from django_filters import rest_framework as filters

from mars_api.models import Game


class GameFilter(filters.FilterSet):
    player_count = filters.NumberFilter()

    class Meta:
        model = Game
        fields = [
            "date",
            "game_map",
            "number_of_generations",
            "draft_variant",
            "prelude",
            "venus_next",
            "colonies",
            "player_count",
        ]
