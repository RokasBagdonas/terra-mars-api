"""Like Transporter but without Jason Statham."""
from sys import stdout

from dateutil import parser
from django.db.utils import IntegrityError

from mars_api.serializers import (GameSerializerForImportedData,
                                  PlayerScoreSerializer)

FIELD_REMAPPING = {
    "game": {"map": "Default"},
    "player_score": {
        "corporation": {
            "Interpl. Cinematics": "Interplanetary Cinematics",
            "UNMI": "United Nations Mars Initiative",
        }
    },
}


def str_to_bool(arg):
    return bool(int(arg))


GAME_FIELD_MAPPING = {
    0: {"id": int},
    1: {"date": parser.parse},  # datetime
    2: {"game_map": str},
    3: {"prelude": str_to_bool},
    4: {"colonies": str_to_bool},
    5: {"number_of_generations": int},
}

PLAYER_SCORE_FIELD_MAPPING = {
    7: {"player_nickname": str},
    8: {"corporation": str},
    10: {"terraform_rating": int},
    11: {"milestones": int},
    12: {"awards": int},
    13: {"greeneries": int},
    14: {"cities": int},
    15: {"event_cards": int},
    16: {"automated_cards": int},
    17: {"active_cards": int},
    18: {"resources": int},
}


def print_status(string):
    stdout.write(f"\u001b[32m{string}\u001b[0m\n")


def print_warning(warning):
    stdout.write(f"\u001b[33mWARNING:\u001b[0m\n{warning}")


def print_error(err):
    stdout.write(format_message(err, colour_code="30;1m"))


def format_message(err, colour_code="48;5;168m"):
    return f"\u001b[{colour_code}{err}\u001b[0m\n"


def import_data(csv_file_path):
    import csv

    games = []
    player_scores = []
    current_game_id = None
    with open(csv_file_path, newline="") as csvfile:
        row_reader = csv.reader(csvfile, delimiter=",")
        print_status("Parsing the csv file")

        for row in row_reader:
            if current_game_id != row[0]:
                current_game_id = row[0]
                games.append(create_game_dict(row))
            player_scores.append(create_player_score_dict(row, current_game_id))

    print_status(f"Number of games: {len(games)}; player scores: {len(player_scores)}")
    save_data(games, player_scores)
    stdout.write(format_message("Import Completed ✅", "\u001b[32;1m"))


def save_data(games_dict, player_scores_dict):
    games_serializer = GameSerializerForImportedData(data=games_dict, many=True)
    ps_serializer = PlayerScoreSerializer(data=player_scores_dict, many=True)
    print_status("Validating the data")

    if not games_serializer.is_valid():
        raise ValueError(format_message(games_serializer.errors))

    print_status("Saving games")
    try:
        games_serializer.save()
    except IntegrityError as err:
        print_warning(err)
        del err

    if not ps_serializer.is_valid():
        raise ValueError(format_message(ps_serializer.errors))

    print_status("Saving scores")
    try:
        ps_serializer.save()
    except IntegrityError as err:
        print_warning(err)
        del err


def list_to_dict(data, mapping):
    """Map a list to a dictionary provided the mapping."""
    dict_ = {}
    for index, prop_type_map in mapping.items():
        name_type = list(prop_type_map.items())
        name = name_type[0][0]
        type_ = name_type[0][1]
        # assign the name to the cast data item
        dict_[name] = type_(data[index])

    return dict_


def create_game_dict(data):
    game_dict = list_to_dict(data, GAME_FIELD_MAPPING)

    if game_dict["game_map"] == FIELD_REMAPPING["game"]["map"]:
        game_dict["game_map"] = "Tharsis"

    return game_dict


def create_player_score_dict(data, game_id):
    ps_dict = list_to_dict(data, PLAYER_SCORE_FIELD_MAPPING)
    ps_dict["game"] = game_id
    ps_dict["player"] = {"nickname": ps_dict["player_nickname"]}

    if ps_dict["corporation"] in FIELD_REMAPPING["player_score"]["corporation"]:
        ps_dict["corporation"] = FIELD_REMAPPING["player_score"]["corporation"][
            ps_dict["corporation"]
        ]

    return ps_dict

