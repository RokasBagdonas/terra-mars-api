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
    """
select count(corporation), corporation from mars_api_playerscore where player_id='1' group by corporation order by count(corporation) desc;
    """
    query = """select corporation, count(corporation) from mars_api_playerscore
               where player_id = %s group by corporation
               order by count(corporation) desc limit 1;
            """
    return fetchone(query, player_id)
