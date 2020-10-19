<template>
<div class="columns">

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
        v-on:click="setPickedGameId(game.id)">
          <td v-for="(value, key) in game" v-bind:key="key">{{ value }}</td>
        </tr>
      </tbody>
    </table>
    </div>
</div>

<div class="column">
    <GameDetails :gameId="pickedGameId"> </GameDetails>
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
        .then(() => console.log(this.games))
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
    isNextDisabled() {
      if (this.currentOffset + this.limit < this.totalNumberOfGames)
        return null;
      else return true;
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
  },
};
</script>


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
