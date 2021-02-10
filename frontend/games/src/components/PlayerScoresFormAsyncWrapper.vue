<template>
  <div class="columns" v-if="playerScores.length > 0">
    <div class="column" v-for="(score, index) in playerScores" :key="index">
      <PlayerScoreForm
        :playerScore="score.value"
        :CORPORATIONS="CORPORATIONS"
        :PLAYERS="PLAYERS"
      />
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
    const { data: CORPORATIONS } = await getCorporations();
    const data = await getPlayers();
    const PLAYERS = data.data.results;
    return {
      CORPORATIONS,
      PLAYERS,
    };
  },
  methods: {
  },
};
</script>
