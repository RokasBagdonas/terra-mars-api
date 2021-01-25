export class PlayerScore {
  terraform_rating: number = 20;
  corporation: string = "";
  player: Player = new Player();
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
  }
}

class Player {
  name: string = "";
  constructor() {

  }
}

