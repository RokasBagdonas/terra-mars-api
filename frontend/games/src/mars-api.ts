import axios from 'axios';

const ROOT_URL = "/mars_api/";

const ENDPOINTS = {
    "games": "games/",
    "players": "players/",
    "player_scores": "player_scores/",
    "game_scores": "game_scores/",
}


export function getGames(limit = 50, offset = 0, order_by="-date") {
    return axios.get(ROOT_URL + ENDPOINTS["games"], {
        params: {
            limit: limit,
            offset: offset,
            ordering: order_by,
        }
    });
}

export function getGameScores(id) {
    return axios.get(ROOT_URL + ENDPOINTS["game_scores"] + id)
}
