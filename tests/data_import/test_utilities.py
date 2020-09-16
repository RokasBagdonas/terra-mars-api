"""Tests for data_importer.py file."""
from datetime import datetime

import pytest
from dateutil import parser

from mars_api.data_import.data_importer import (
    create_game_dict,
    create_player_score_dict,
    list_to_dict,
)
from mars_api.models import Game, PlayerScore


def test_list_to_dict():
    time = datetime.now()
    list_ = ["one", "2", str(time)]
    mapping = {(0, "field1", str), (1, "field2", int), (2, "field3", parser.parse)}

    assert list_to_dict(list_, mapping) == {
        "field1": "one",
        "field2": 2,
        "field3": time,
    }


def test_create_game(game_dict_factory):
    game_dict = game_dict_factory()
    game_dict["id"] = 1
    data = [
        str(game_dict["id"]),
        str(game_dict["date"]),
        str(game_dict["game_map"]),
        str(int(game_dict["prelude"])),
        str(int(game_dict["colonies"])),
        str(game_dict["number_of_generations"]),
    ]

    g = create_game_dict(data)
    assert g["id"] == game_dict["id"]
    assert g["date"] == game_dict["date"]
    assert g["game_map"] == game_dict["game_map"]


def test_create_game_dict_with_default_map(game_dict_factory):
    game_dict = game_dict_factory()
    game_dict["id"] = 1
    game_dict["game_map"] = "Tharsis"
    data = [
        str(game_dict["id"]),
        str(game_dict["date"]),
        str("Default"),
        str(int(game_dict["prelude"])),
        str(int(game_dict["colonies"])),
        str(game_dict["number_of_generations"]),
    ]

    g = create_game_dict(data)
    assert g["id"] == game_dict["id"]
    assert g["date"] == game_dict["date"]
    assert g["game_map"] == game_dict["game_map"]


def test_create_player_score(player_score_dict_factory, game_dict_factory):
    game_dict = game_dict_factory()
    game_dict["id"] = 1
    ps_dict = player_score_dict_factory()
    ps_dict["player"]["nickname"] = "Greta"
    ps_dict["corporation"] = "Ecoline"
    data = [
        "98",
        "2019-03-16",
        "Elysium",
        "1",
        "0",
        "11",
        "3",
        "Greta",
        "Ecoline",
        "0",
        "42",
        "5",
        "2",
        "12",
        "17",
        "0",
        "9",
        "0",
        "10",
        "97",
    ]

    ps = create_player_score_dict(data, game_dict["id"])
    assert ps["player"]["nickname"] == ps_dict["player"]["nickname"]
    assert ps["corporation"] == ps_dict["corporation"]
