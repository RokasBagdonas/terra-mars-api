<template>
  <div class="section">
    <div class="level">
      <div class="level-item">
        <button class="button is-primary" type="button" @click="submitGame">
          Add Game
        </button>
      </div>
      <div class="modal" :class="{ 'is-active': submitted }">
        <div class="modal-background"></div>
        <div class="modal-content">
          <div class="box">
            <p v-if="submitStatus == '201'">Successfully submitted :)</p>
            <p v-else>
              <vue-json-pretty :data="submitStatus" />
            </p>
          </div>
        </div>
        <button
          class="modal-close is-large"
          aria-label="close"
          @click="submitted = false"
        ></button>
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
  <div class="level">
    <div class="level-left">
      <div class="level-item">
        <BaseNumberInput
          label="number of players?"
          v-model="numberOfPlayers"
          type="number"
        />
      </div>
      <div class="level-item">
        <button type="button" class="button" @click="submitNumberOfPlayers">
          confirm
        </button>
      </div>
    </div>
  </div>
  <Suspense v-if="submittedNumberOfPlayers">
    <template #default>
      <PlayerScoresFormAsyncWrapper :playerScores="playerScores" />
    </template>
    <template #fallback>Preparing player scores form...</template>
  </Suspense>
</template>


<script>
/*'use-strict';*/
import { ref, unref, toRaw, isRef } from "vue";
import VueJsonPretty from "vue-json-pretty";
import "vue-json-pretty/lib/styles.css";

import { Game, PlayerScore } from "../classes";
import { postGameScores } from "../mars-api";
import GameFormAsyncWrapper from "../components/GameFormAsyncWrapper";
import PlayerScoresFormAsyncWrapper from "../components/PlayerScoresFormAsyncWrapper";

export default {
  components: {
    GameFormAsyncWrapper,
    PlayerScoresFormAsyncWrapper,
    VueJsonPretty,
  },
  setup() {
    let playerScores = ref([]);
    let game = ref(new Game());
    game.value.number_of_generations = 10;
    let numberOfPlayers = 2;
    let submittedNumberOfPlayers = new ref(null);
    let submitStatus = null;
    let submitted = ref(false);
    return {
      playerScores,
      game,
      numberOfPlayers,
      submittedNumberOfPlayers,
      submitStatus,
      submitted,
    };
  },
  methods: {
    async submitGame() {
      console.log(this.canSubmitGame());
      if (!this.canSubmitGame()) {
        this.submitStatus = JSON.parse(
          '{ "error": "number of players is invalid" }'
        );
        this.submitted = true;
        return;
      }
      let payload = this.objectToDictionary(this.game);
      payload["scores"] = this.unrefArray(this.playerScores);
      await postGameScores(JSON.stringify(payload))
        .then((response) => {
          console.log("response", response);
          this.submitStatus = response.status;
          this.submitted = true;
        })
        .catch((error) => {
          console.error(error);
          console.log(error.response);
          this.submitStatus = error.response;
          this.submitted = true;
        });
    },
    canSubmitGame() {
      let allowSubmit = false;
      const ps = this.unrefArray(this.playerScores);
      if (ps.length >= 1 && ps.length <= 5) {
        allowSubmit = true;
      }
      console.log("allowSubmit", allowSubmit);
      return allowSubmit;
    },
    submitNumberOfPlayers() {
      if (this.numberOfPlayers < 1 || this.numberOfPlayers > 5) {
        // TODO: display warning
        console.error("Invalid number of players: " + this.numberOfPlayers);
      }
      this.submittedNumberOfPlayers = this.numberOfPlayers;

      // diff
      let diffnp = this.numberOfPlayers - this.playerScores.length;
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
