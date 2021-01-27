// for encapsulating data in input form
export class PlayerScore {
  player: Player = new Player();
  corporation: string = "";
  terraform_rating: number = 20;
  milestones: number = 0;
  awards: number = 0;
  greeneries: number = 0;
  cities: number = 0;
  event_cards: number = 0;
  automated_cards: number = 0;
  active_cards: number = 0;
  resources: number = 0;
  total_score: number = 0;
  is_winner: boolean = false;

  constructor() {
  };

}

//export const PLAYER_SCORE_SCHEMA = {
  //player: {
    //label: "player",
    //component: "BaseSelect"
  //},
  //corporation: {
    //label: "corporation",
    //component: "BaseSelect",
  //},
  //terraform_rating: {
    //label: "TR",
    //component: "BaseInput",
    //type: "number",
  //},
  //milestones: {
    //label: "milestones",
    //component: "BaseInput",
    //type: "number",
  //},
  //awards: {
    //label: "awards",
    //component: "BaseInput",
    //type: "number",
  //},
  //greeneries: {
    //label: "greeneries",
    //component: "BaseInput",
    //type: "number",
  //},
  //cities: {
    //label: "cities",
    //component: "BaseInput",
    //type: "number",
  //},
  //event_cards: {
    //label: "events",
    //component: "BaseInput",
    //type: "number",
  //},
  //automated_cards: {
    //label: "automated cards",
    //component: "BaseInput",
    //type: "number",
  //},
  //active_cards: {
    //label: "active cards",
    //component: "BaseInput",
    //type: "number",
  //},
  //resources: {
    //label: "resources",
    //component: "BaseInput",
    //type: "number",
  //},
  //total_score: {
    //label: "total score",
    //component: "BaseInput",
    //type: "number",
  //},
  //is_winner: {
    //label: "is winner",
    //component: "BaseInput",
    //type: "number",
  //},

//}

class Player {
  name: string = "";
  constructor() {

  }
}

