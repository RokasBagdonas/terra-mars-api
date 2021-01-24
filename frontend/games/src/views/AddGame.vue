<template>
  <h1>Add Game</h1>
  <p>AddGame TR: {{score}}</p>
  <PlayerScoreForm :playerScore="score"/>
</template>


<script>
import PlayerScoreForm from "../components/PlayerScoreForm";
import { PlayerScore } from "../classes";

export default {
  components: {
    PlayerScoreForm,
  },
  data() {
    return {
      scores: [new PlayerScore()],
      score: new PlayerScore(),
    };
  },
};
</script>
