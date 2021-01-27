<template>
  <h1>Add Game</h1>
  <BaseInput
    label="number of players"
    v-model="numberOfPlayers"
    type="number"
  />
  <button type="button" @click="submitNumberOfPlayers">submit</button>

  <div class="columns" v-if="scores.length > 0">
    <div class="column" v-for="(score, index) in scores" :key="index">
      <PlayerScoreForm :playerScore="score.value" />
    </div>
  </div>
</template>


<script>
import { ref } from "vue";
import { PlayerScore } from "../classes";
import PlayerScoreForm from "../components/PlayerScoreForm";

export default {
  components: {
    PlayerScoreForm,
  },
  data() {
    return {
      scores: [],
      score: new PlayerScore(),
      numberOfPlayers: 0,
    };
  },
  methods: {
    submitNumberOfPlayers() {
      this.scores.length = 0;
      for (let i = 0; i < this.numberOfPlayers; i++) {
        this.scores.push(ref(new PlayerScore()));
      }
    },
  },
};
</script>
