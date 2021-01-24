<template>
  <h1>Add Game</h1>
  <BaseInput label="number of players" v-model="numberOfPlayers" type="number"/>

  <PlayerScoreForm :playerScore="score"/>
</template>


<script>
import BaseInput from "../components/form-components/BaseInput";
import PlayerScoreForm from "../components/PlayerScoreForm";
import { PlayerScore } from "../classes";

export default {
  components: {
    PlayerScoreForm,
    BaseInput,
  },
  data() {
    return {
      scores: [new PlayerScore()],
      score: new PlayerScore(),
      numberOfPlayers: 0,
    };
  },
};
</script>
