from dateutil import parser

from mars_api.serializers import GameSerializer, PlayerScoreSerializer

FIELD_REMAPPING = {
    "game": {"map": "Default"},
    "player_score": {
        "corporation": {
            "Interpl. Cinematics": "Interplanetary Cinematics",
            "UMNI": "United Nations Mars Initiative",
        }
    },
}

GAME_FIELD_MAPPING = {
    0: {"id": int},
    1: {"date": parser.parse},  # datetime
    2: {"game_map": str},
    3: {"prelude": bool},
    4: {"colonies": bool},
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


def import_data(csv_file_path):
    import csv

    games = []
    player_scores = []
    current_game_id = None
    with open(csv_file_path, newline="") as csvfile:
        row_reader = csv.reader(csvfile, delimiter=",")

        for row in row_reader:
            if current_game_id != row[0]:
                current_game_id = row[0]
                games.append(create_game_dict(row))
            player_scores.append(create_player_score_dict(row, current_game_id))

    # add games and player_scores
    save_games(games)
    save_player_scores(player_scores)


def save_games(games_dict):
    games_serializer = GameSerializer(data=games_dict, many=True)
    if not games_serializer.is_valid():
        print(games_serializer.errors)

    games_serializer.save()


def save_player_scores(ps_dict):
    ps_serializer = PlayerScoreSerializer(data=ps_dict, many=True)
    if not ps_serializer.is_valid():
        print(ps_serializer.errors)

    ps_serializer.save()


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
