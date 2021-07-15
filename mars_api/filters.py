from django_filters import rest_framework as filters

from mars_api.models import Game, PlayerScore, PlayerStats


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


class PlayerStatsFilter(filters.FilterSet):

    class Meta:
        model = PlayerStats
        fields = [
            "games_played",
            "win_percentage",
            "most_popular_corporation",
            "average_number_of_players_in_games",
            "last_updated",
        ]

