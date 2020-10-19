<template>
    <div class="is-child box" id="table-cont">
  <div class="table-container">
  <table class="table is-hoverable">
    <thead>
      <tr>
        <th
          v-for="(display_name, model_name) in PLAYER_SCORE_SCHEMA"
          v-bind:key="model_name"
        >{{display_name}}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="playerScore in gameScores.scores" v-bind:key="playerScore">
        <td
          v-for="(display_name, model_name) in PLAYER_SCORE_SCHEMA"
          v-bind:key="playerScore"
        >{{getDisplayName(playerScore, model_name)}}</td>
      </tr>
    </tbody>
  </table>
  </div>
  </div>
</template>


<script>
import Vue from "vue";
import { PLAYER_SCORE_SCHEMA } from "../mars-api";
export default {
  props: ["gameScores"],
  data() {
    return {
      PLAYER_SCORE_SCHEMA: PLAYER_SCORE_SCHEMA,
    };
  },
  methods: {
    getDisplayName(playerScore, prop_name) {
        console.log(prop_name);
      if (prop_name !== "player") return playerScore[prop_name];
      else return playerScore[prop_name].nickname;
    },
  },
};
</script>

<style lang="scss" scoped>
#table-cont {
overflow-x: auto;
}
</style>
