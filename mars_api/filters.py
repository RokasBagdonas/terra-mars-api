from django_filters import rest_framework as filters

from mars_api.models import Game, PlayerScore


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
            # "player_count",
        ]


class PlayerScoreFilter(filters.FilterSet):

    player__nickname = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = PlayerScore
        fields = [
            "game",
            "player",
            "corporation",
            "terraform_rating",
            "milestones",
            "awards",
            "greeneries",
            "cities",
            "event_cards",
            "automated_cards",
            "active_cards",
            "resources",
        ]
