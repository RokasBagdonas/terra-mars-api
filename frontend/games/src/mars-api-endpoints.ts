import axios from 'axios';

const ROOT_URL = "/mars_api/";

const ENDPOINTS = {
    "games": "games/",
    "players": "players/",
    "player_scores": "player_scores/"
}


export function getAllGames() {
    console.log("get all games!!");
    return axios.get(ROOT_URL + ENDPOINTS["games"]);
}
