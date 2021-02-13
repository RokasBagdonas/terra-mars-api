import axios from 'axios';

const ROOT_URL = "/mars_api/";

const ENDPOINTS = {
  "games": "games/",
  "players": "players/",
  "player_scores": "player_scores/",
  "game_scores": "game_scores/",
  "corporations": "corporations",
  "maps": "maps"
}

export const GAME_SCHEMA = {
  Id: "id",
  "Player #": "player_count",
  Date: "date",
  Map: "game_map",
  "Gen #": "number_of_generations",
  Draft: "draft",
  Prelude: "prelude",
  "Venus Next": "venus_next",
  Colonies: "colonies",

}

export const PLAYER_SCORE_SCHEMA = {
  player: "Player", //player object
  corporation: "Corporation",
  terraform_rating: "TR",
  milestones: "Milestones",
  awards: "Awards",
  greeneries: "Greeneries",
  cities: "Cities",
  event_cards: "Events",
  automated_cards: "Automoated cards",
  active_cards: "Active cards",
  resources: "Resources",
  total_score: "Final Score",
  is_winner: "Won?",
  id: "score_id",
  game_id: "game_id"
}


export function getGames(limit = 50, offset = 0, order_by = "-date") {
  return axios.get(ROOT_URL + ENDPOINTS["games"], {
    params: {
      limit: limit,
      offset: offset,
      ordering: order_by,
    }
  });
}

export function getGameScores(id) {
  return axios.get(ROOT_URL + ENDPOINTS["game_scores"] + id);
}

export async function getPlayers(){
  return axios.get(ROOT_URL + ENDPOINTS["players"]);
}


export async function getMaps() {
  return await axios.get(ROOT_URL + ENDPOINTS["maps"]);
}

export async function getCorporations() {
  return await axios.get(ROOT_URL + ENDPOINTS["corporations"]);
}

export function postGameScores(payload: String) {
  console.log("postGameScores");
  return axios({
    url: ROOT_URL + ENDPOINTS["game_scores"], data: payload, method: "post", headers:
    {
      "Content-Type": "application/json"
    }
  })
}
