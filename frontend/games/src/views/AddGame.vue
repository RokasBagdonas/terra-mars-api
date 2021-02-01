<template>
  <h1>Add Game</h1>
  <p>{{ playerScores }}</p>
  <Suspense>
    <template #default>
      <GameFormAsyncWrapper :game="game"/>
    </template>
    <template #fallback>Preparing game form...</template>
  </Suspense>

  <Suspense>
    <template #default>
      <PlayerScoresFormAsyncWrapper :playerScores="playerScores"/>
    </template>
    <template #fallback>Preparing player scores form...</template>
  </Suspense>
</template>


<script>
import { ref } from "vue";

import { PlayerScore } from "../classes";
import GameFormAsyncWrapper from "../components/GameFormAsyncWrapper";
import PlayerScoresFormAsyncWrapper from "../components/PlayerScoresFormAsyncWrapper";

export default {
  components: {
    GameFormAsyncWrapper,
    PlayerScoresFormAsyncWrapper
  },
  setup() {
    let playerScores = ref([]);
    let game = ref({});
    return {
      playerScores,
      game
    };
  },
};
</script>
