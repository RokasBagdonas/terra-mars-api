<template>
  <div class="section">
    <div class="level">
      <div class="level-left">
        <div class="level-item">
          <h1 class="title is-3">Add Game</h1>
        </div>
        <div class="level-item">
          <button class="button is-primary" type="button" @click="submitGame">
            Submit
          </button>
        </div>
      </div>
    </div>
  </div>
  <!--
  <p> {{ game }}</p>
  <p>{{ playerScores }}</p>
  -->

  <Suspense>
    <template #default>
      <GameFormAsyncWrapper :game="game" />
    </template>
    <template #fallback>Preparing game form...</template>
  </Suspense>

  <Suspense>
    <template #default>
      <PlayerScoresFormAsyncWrapper :playerScores="playerScores" />
    </template>
    <template #fallback>Preparing player scores form...</template>
  </Suspense>
</template>


<script>
import { ref, unref, toRaw, isRef } from "vue";

import { Game } from "../classes";
import { postGameScores } from "../mars-api";
import GameFormAsyncWrapper from "../components/GameFormAsyncWrapper";
import PlayerScoresFormAsyncWrapper from "../components/PlayerScoresFormAsyncWrapper";

export default {
  components: {
    GameFormAsyncWrapper,
    PlayerScoresFormAsyncWrapper,
  },
  setup() {
    let playerScores = ref([]);
    let game = ref(new Game());
    return {
      playerScores,
      game,
    };
  },
  methods: {
    submitGame() {
      //TODO: validation
      let payload = this.objectToDictionary(this.game);
      payload["scores"] = this.unrefArray(this.playerScores);
      postGameScores(JSON.stringify(payload));
    },
    unrefArray(arr) {
      if (arr.length === 0) {
        return arr;
      }
      let result = [];
      for (let item of arr) {
        result.push(item.value);
      }
      return result;
    },
    objectToDictionary(obj) {
      let dict = {};
      for (let prop in obj) {
        dict[prop] = obj[prop];
        console.log(prop);
      }
      return dict;
    },
  },
};
</script>
