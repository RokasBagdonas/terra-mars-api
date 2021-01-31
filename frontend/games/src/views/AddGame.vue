<template>
  <h1>Add Game</h1>
  <p>corps: {{ CORPORATIONS }}</p>
  <p>maps: {{ MAPS }}</p>
  <p>{{ scores }}</p>
  <BaseInput
    label="number of players"
    v-model="numberOfPlayers"
    type="number"
  />
  <button type="button" @click="submitNumberOfPlayers">submit</button>
  <!--
  <Promised :promise="corporationsPromise">
    <template v-slot:pending>
      <p>Loading...</p>
    </template>
    <template v-slot="data">
      <p>data: {{ data }}</p>
    </template>
    <template v-slot:rejected="error">
      <p>Error: {{ error.message }}</p>
    </template>
  </Promised>
  -->
  <div class="columns" v-if="scores.length > 0">
    <div class="column" v-for="(score, index) in scores" :key="index">
      <PlayerScoreForm :playerScore="score.value" />
    </div>
  </div>
</template>


<script>
import { ref } from "vue";
/*import { Promised, usePromise } from "promised";*/

import { PlayerScore } from "../classes";
import PlayerScoreForm from "../components/PlayerScoreForm";
import { getCorporations, getMaps } from "../mars-api";

export default {
  components: {
    PlayerScoreForm,
  },
  /*data() {*/
    /*return {*/
      /*corporationsPromise: null,*/
    /*};*/
  /*},*/
  /*created() {*/
    /*this.corporationsPromise = this.getCorporations();*/
  /*},*/
  setup() {
    let scores = ref([]);
    let numberOfPlayers = ref(0);
    return {
      scores,
      numberOfPlayers,
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
