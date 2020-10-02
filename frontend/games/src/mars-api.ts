import axios from 'axios';

const ROOT_URL = "/mars_api/";

const ENDPOINTS = {
    "games": "games/",
    "players": "players/",
    "player_scores": "player_scores/"
}


export function getAllGames(limit = 50, offset = 0) {
    return axios.get(ROOT_URL + ENDPOINTS["games"], {
        params: {
            limit: limit,
            offset: offset
        }
    });
}
