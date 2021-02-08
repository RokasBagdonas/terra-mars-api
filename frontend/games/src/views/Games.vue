<template>
<div class="columns">

<div class="box">
<div class="column">
    <div class="container">
        <a
          class="pagination-previous"
          v-on:click="this.navigateGames(false)"
          v-bind:disabled="isPreviousDisabled"
        >Previous</a>
        <a
          class="pagination-next"
          v-on:click="this.navigateGames(true)"
          v-bind:disabled="isNextDisabled"
        >Next</a>
    </div>
    <div class="table-container">
    <table class="table is-striped is-hoverable is-narrow">
      <thead>
        <tr>
          <th
            v-for="(prop_name, display_name) in this.GAME_SCHEMA"
            v-on:click="sortTable(prop_name)"
            v-bind:key="prop_name"
          >{{display_name}}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="game in games" v-bind:key="game"
        @click="setPickedGameId(game.id)">
          <td v-for="(value, key) in game">{{ value }}</td>
        </tr>
      </tbody>
    </table>
    </div>
</div>
</div>
<div class="column">
    <GameDetails v-if="pickedGameId" :gameId="pickedGameId"> </GameDetails>
</div>
</div>
</template>

<script>
import { getGames, getGameScores, GAME_SCHEMA } from "../mars-api";
import GameDetails from "../components/GameDetails.vue";
let limit = 50;
let currentoffset = 0;

export default {
  components: { GameDetails },
  data() {
    return {
      games: [],
      limit: 50,
      currentOffset: 0,
      orderByName: "date",
      orderByDirection: "-",
      totalNumberOfGames: 0,
      pickedGameId: undefined,
      GAME_SCHEMA: GAME_SCHEMA, //from mars-api.ts
      tableSortParams: {
        ascending: false,
        sortColumn: "",
      },
    };
  },
  methods: {
    // API calls --------------------------------------------------------------
    fetchGames(order_by = this.getOrderByName()) {
      order_by = this.getOrderByName();
      getGames(this.limit, this.currentOffset, order_by)
        .then((response) => {
          this.totalNumberOfGames = response.data.count;
          this.games = response.data.results;
        })
        .catch((error) => console.log(error));
    },
    setPickedGameId(gameId){
        this.pickedGameId = gameId;
    },
    // Pagination -------------------------------------------------------------
    navigateGames(forward) {
      if (forward) {
        if (this.currentOffset + this.limit < this.totalNumberOfGames)
          this.currentOffset += this.limit;
      } else {
        if (this.currentOffset <= this.limit) this.currentOffset = 0;
        else this.currentOffset -= this.limit;
      }
      this.fetchGames();
    },
    // Filtering --------------------------------------------------------------
    getOrderByName() {
      return this.orderByDirection + this.orderByName;
    },
    toggleOrderByDirection() {
      if (this.orderByDirection === "-") {
        this.orderByDirection = "";
      } else this.orderByDirection = "-";
    },
    setOrderByName(name) {
      if (name === this.orderByName) {
        this.toggleOrderByDirection();
      } else {
        this.orderByName = name;
        this.orderByDirection = "";
      }
    },
    sortTable(name) {
      console.log("sort table event");
      this.setOrderByName(name);
      this.fetchGames(name);
    },
  },
  // Vue lifecycle ------------------------------------------------------------
  created: function () {
    console.log("created hook");
  },
  mounted: function () {
    this.fetchGames();
  },
  computed: {
    isPreviousDisabled() {
      if (this.currentOffset >= this.limit) return null;
      else return true;
    },
    isNextDisabled() {
      if (this.currentOffset + this.limit < this.totalNumberOfGames)
        return null;
      else return true;
    },
  },
};
</script>

<!--
WARNING in ./src/views/Games.vue?vue&type=style&index=0&id=dfa49f12&lang=scss&module=true&scoped=true 1:0-402
export 'default' (reexported as 'default') was not found in '-!../../node_modules/mini-css-extract-plugin/dist/loader.js!../../node_modules/css-loader/dist/cjs.js!../../node_modules/vue-loader/dist/stylePostLoader.js!../../node_modules/sass-loader/dist/cjs.js??clonedRuleSet-3.use[2]!../../node_modules/vue-loader/dist/index.js??ruleSet[1].rules[6].use[0]!./Games.vue?vue&type=style&index=0&id=dfa49f12&lang=scss&module=true&scoped=true' (possible exports: )
<style lang="scss" module scoped>
th {
  cursor: pointer;
}
th:hover {
  background-color: lavender;
}
tr {
  cursor: pointer;
}
.clicked {
    background-color: lavender;
}
</style>
-->
