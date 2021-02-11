<template>
  <div class="section">
    <div class="level">
      <div class="level-left">
        <div class="level-item">
          <h1 class="title is-3">Add Game</h1>
        </div>
        <div class="level-item">
          <button class="button is-primary" type="button" @click="submitGame">Submit</button>
        </div>

        <div class="level-item">
          <BaseNumberInput label="number of players?" v-model="numberOfPlayers" type="number" />
        </div>
        <div class="level-item">
          <button type="button" class="button" @click="submitNumberOfPlayers">confirm</button>
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
  <Suspense v-if="submittedNumberOfPlayers">
    <template #default>
      <PlayerScoresFormAsyncWrapper :playerScores="playerScores" />
    </template>
    <template #fallback>Preparing player scores form...</template>
  </Suspense>
</template>


<script>
'use-strict';
import { ref, unref, toRaw, isRef } from "vue";

import { Game, PlayerScore } from "../classes";
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
    game.value.number_of_generations = 10;
    let numberOfPlayers = 2;
    let submittedNumberOfPlayers = new ref(null);
    return {
      playerScores,
      game,
      numberOfPlayers,
      submittedNumberOfPlayers,
    };
  },
  methods: {
    submitGame() {
      //TODO: validation
      let payload = this.objectToDictionary(this.game);
      payload["scores"] = this.unrefArray(this.playerScores);
      postGameScores(JSON.stringify(payload));
    },

    submitNumberOfPlayers() {
      if (this.numberOfPlayers < 1 || this.numberOfPlayers > 5) {
        // TODO: display warning
        console.error("Invalid number of players: " + this.numberOfPlayers);
      }
      this.submittedNumberOfPlayers = this.numberOfPlayers;

      // diff
      let diffnp = this.numberOfPlayers - this.playerScores.length;
      // 5 - 0 = 5
      if (diffnp > 0) {
        for (let i = 0; i < diffnp; i++) {
          this.playerScores.push(ref(new PlayerScore()));
        }
      }
      if (diffnp < 0) {
        for (let i = 0; i > diffnp; i--) {
          this.playerScores.pop();
        }
      }
    },

    // --- Utilities ---
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
