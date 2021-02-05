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

export class Game {
  date: Date = new Date();
  game_map: string = "Tharsis";
  number_of_generations: number;
  draft_variant: boolean = false;
  prelude: boolean = false;
  venus_next: boolean = false;
  colonies: boolean = false;
}

export class Player {
  nickname: string = "";

  static playersToNicknameList(players: Array<Player>){
    let result = new Array<String>();
    for(let p of players){
      result.push(p.nickname);
    }
    return result;
  }
}
