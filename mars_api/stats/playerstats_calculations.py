from decimal import Decimal

from mars.db_helper import fetchone
from mars_api.models import PlayerScore


def get_games_played(player_id):
    return PlayerScore.objects.filter(player=player_id).count()


def get_player_win_percentage(player_id, games_played=None):
    # number of games played divided by PlayerScore games won count
    if not games_played or games_played <= 0:
        return None

    games_won = (
        PlayerScore.objects.filter(player_id=player_id).filter(is_winner=True).count()
    )
    return Decimal(games_won) / games_played


# TODO: make this an endpoint (get count of corporations)
def get_most_popular_corporation(player_id):
    query = """select corporation, count(corporation) from mars_api_playerscore
               where player_id = %s group by corporation
               order by count(corporation) desc limit 1;
            """
    return fetchone(query, player_id)


def get_average_number_of_players_in_games(player_id):
    # 1. Count number of players in each game

    # 2. num of players / num of games
    query = """
            -- 3. get average
            select avg(count) from
                -- 2. Count how many players there were in each game
                (select count(*) from mars_api_playerscore where game_id in
                    -- 1. get games that player played in
                    (select game_id from mars_api_playerscore where player_id = %s) group by game_id
                ) number_of_players;
            """

    return fetchone(query, player_id)[0]
