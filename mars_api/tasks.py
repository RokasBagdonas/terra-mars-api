from celery import shared_task
from mars_api.models import Player, PlayerStats
from mars_api.stats import playerstats_calculations as psc


# TODO: make async
@shared_task
def update_player_stats(player_id):
    print("update_player_stats with player_id: " + str(player_id))
    try:
        ps, _ = PlayerStats.objects.get_or_create(player_id=player_id)

        # 1. games played
        ps.games_played = psc.get_games_played(player_id)

        # 2. win percentage
        ps.win_percentage = psc.get_player_win_percentage(player_id, ps.games_played)

        # 3. most popular corporation
        ps.most_popular_corporation = psc.get_most_popular_corporation(player_id)

        # 4. (average) number of players in games
        ps.average_number_of_players_in_games = psc.get_average_number_of_players_in_games(player_id)

        ps.save()
        print(ps)
        return ps

    except Exception as e:
        print(e)


@shared_task
def calc_all_player_stats():
    player_ids = list(map(lambda p: p.id, Player.objects.all()))
    print("calc_all_player_stats with ids: " + str(player_ids))
    for id in player_ids:
        update_player_stats(id)


# test
@shared_task
def count_players():
    count = Player.objects.count()
    print("=== counted players: " + str(count))
    return Player.objects.count()
