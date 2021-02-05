<template>
  <h5 class="title is-5">Player Scores</h5>
  <BaseInput label="number of players" v-model="numberOfPlayers" type="number"/>
  <button type="button" @click="submitNumberOfPlayers">submit</button>

  <div class="columns" v-if="playerScores.length > 0">
    <div class="column" v-for="(score, index) in playerScores" :key="index">
      <PlayerScoreForm :playerScore="score.value" :CORPORATIONS="CORPORATIONS"
      :PLAYERS="PLAYERS"/>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import PlayerScoreForm from "./PlayerScoreForm";
import { getPlayers, getCorporations } from "../mars-api";
import { PlayerScore } from "../classes";

export default {
  props: {
    playerScores: {
      type: Array,
      required: true,
    },
  },
  components: {
    PlayerScoreForm,
  },
  async setup() {
    const {data: CORPORATIONS} = await getCorporations();
    const data = await getPlayers();
    const PLAYERS = data.data.results;
    let numberOfPlayers = 3;
    return {
      CORPORATIONS,
      PLAYERS,
      numberOfPlayers
    };
  },
  methods: {
    submitNumberOfPlayers() {
      this.playerScores.length = 0;
      for (let i = 0; i < this.numberOfPlayers; i++) {
        this.playerScores.push(ref(new PlayerScore()));
      }
    },
  },
};
</script>
