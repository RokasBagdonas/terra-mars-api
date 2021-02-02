<template>
  <h3>PlayerScoreFormAsyncWrapper</h3>
  <BaseInput label="number of players" v-model="numberOfPlayers" type="number"/>
  <button type="button" @click="submitNumberOfPlayers">submit</button>

  <div class="columns" v-if="playerScores.length > 0">
    <div class="column" v-for="(score, index) in playerScores" :key="index">
      <PlayerScoreForm :playerScore="score.value" :CORPORATIONS="CORPORATIONS"/>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import PlayerScoreForm from "./PlayerScoreForm";
import { getCorporations } from "../mars-api";
import { PlayerScore  } from "../classes";

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
    let numberOfPlayers = 3;
    return {
      CORPORATIONS,
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
