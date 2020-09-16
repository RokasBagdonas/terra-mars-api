from typing import Dict

import colorlog
from dateutil import parser
from django.db.utils import IntegrityError

from mars_api.serializers import GameSerializerForImportedData, PlayerScoreSerializer


def str_to_bool(arg):
    return bool(int(arg))


GAME_FIELD_MAPPING = {
    (0, "id", int),
    (1, "date", parser.parse),  # datetime
    (2, "game_map", str),
    (3, "prelude", str_to_bool),
    (4, "colonies", str_to_bool),
    (5, "number_of_generations", int),
}

GAME_VALUE_REMAPPING = {"Default": "Tharsis"}

PLAYER_SCORE_FIELD_MAPPING = {
    (7, "player_nickname", str),
    (8, "corporation", str),
    (10, "terraform_rating", int),
    (11, "milestones", int),
    (12, "awards", int),
    (13, "greeneries", int),
    (14, "cities", int),
    (15, "event_cards", int),
    (16, "automated_cards", int),
    (17, "active_cards", int),
    (18, "resources", int),
}

PLAYER_SCORE_VALUE_REMAPPING = {
    "UNMI": "United Nations Mars Initiative",
    "Interpl. Cinematics": "Interplanetary Cinematics",
}


def remap_values(data: Dict[str, any], remapping: Dict[any, any]):
    return {
        key: (
            remapping[value]
            if not isinstance(value, list)
            and not isinstance(value, dict)
            and value in remapping
            else value
        )
        for key, value in data.items()
    }


# setup the logger
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter("%(log_color)s%(levelname)s: %(message)s"))

logger = colorlog.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel("INFO")


def import_data(csv_file_path):
    import csv

    games = []
    player_scores = []
    current_game_id = None
    with open(csv_file_path, newline="") as csvfile:
        row_reader = csv.reader(csvfile, delimiter=",")
        logger.info("Parsing csv file: '%s'" % csvfile.name)

        for row in row_reader:
            if current_game_id != row[0]:
                current_game_id = row[0]
                games.append(create_game_dict(row))
            player_scores.append(create_player_score_dict(row, current_game_id))

    logger.info(f"Number of games: {len(games)}; player scores: {len(player_scores)}")
    save_data(games, player_scores)
    logger.info("Import Completed ✅")


def save_data(games_dict, player_scores_dict):
    games_serializer = GameSerializerForImportedData(data=games_dict, many=True)
    ps_serializer = PlayerScoreSerializer(data=player_scores_dict, many=True)
    logger.info("Validating the data")

    if not games_serializer.is_valid():
        logger.error(games_serializer.errors)
        raise ValueError

    logger.info("Saving games")
    try:
        games_serializer.save()
    except IntegrityError as err:
        logger.warning(err)
        del err

    if not ps_serializer.is_valid():
        logger.error(ps_serializer.errors)
        raise ValueError

    logger.info("Saving scores")
    try:
        ps_serializer.save()
    except IntegrityError as err:
        logger.warning(err)
        del err


def list_to_dict(data, mapping):
    return {field: cast_func(data[idx]) for idx, field, cast_func in mapping}


def create_game_dict(data):
    game_dict = list_to_dict(data, GAME_FIELD_MAPPING)
    game_dict = remap_values(game_dict, GAME_VALUE_REMAPPING)

    return game_dict


def create_player_score_dict(data, game_id):
    ps_dict = list_to_dict(data, PLAYER_SCORE_FIELD_MAPPING)
    ps_dict["game"] = game_id
    ps_dict["player"] = {"nickname": ps_dict["player_nickname"]}

    ps_dict = remap_values(ps_dict, PLAYER_SCORE_VALUE_REMAPPING)

    return ps_dict
