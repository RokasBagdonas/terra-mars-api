from mars_api.models import PlayerScore
from mars.db_helper import fetchone


def get_games_played(player_id):
    return PlayerScore.objects.filter(player=player_id).count()


def get_player_win_percentage(player_id, games_played=None):
    # number of games played divided by PlayerScore games won count
    if not games_played:
        return None

    games_won = (
        PlayerScore.objects.filter(player_id=player_id).filter(is_winner=True).count()
    )
    return games_won


# TODO: make this an endpoint (get count of corporations)
def get_most_popular_corporation(player_id):
    """
select count(corporation), corporation from mars_api_playerscore where player_id='1' group by corporation order by count(corporation) desc;
    """
    query = """select top 1 corporation, count(corporation) from mars_api_playerscore
               where player_id = %s group by corporation
               order by count(corporation) desc;
            """
    return fetchone(query, player_id)
