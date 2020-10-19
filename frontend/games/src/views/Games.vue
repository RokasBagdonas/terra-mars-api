<template>
  <div class="tile is-ancestor">
    <div class="tile is-6 is-vertical is-parent">
      <div class="tile is-child pagination is-centered">
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

      <div class="table-container is-child box">
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
            v-on:click="fetchGameScores(game.id)">
              <td v-for="(value, key) in game" v-bind:key="key">{{ value }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="tile is-vertical is-parent">
        <GameDetails :gameScores="pickedGame" :limit="limit"> </GameDetails>
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
      pickedGame: undefined,
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
    fetchGameScores(id) {
      console.log("fetchGameScores");
      getGameScores(id)
        .then((response) => {
          this.pickedGame = response.data;
          console.log(response.data);
        })
        .catch((error) => console.log(error));
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
