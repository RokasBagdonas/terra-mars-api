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
        <table class="table is-striped is-hoverable">
          <thead>
            <tr>
              <th
                v-for="(prop_name, display_name) in GAME_SCHEMA"
                v-on:click="sortTable(prop_name)"
                v-bind:key="prop_name"
              > {{display_name}} </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="game in games" v-bind:key="game" v-on:click="fetchGameScores(game.id)">
              <td v-for="(value, key) in game" v-bind:key="key">{{ value }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="tile is-vertical is-parent">
      <div class="tile box is-child">
        <!-- <GameDetails gameScores="this.pickedGame"></GameDetails> -->
      </div>
    </div>
  </div>
</template>

<script>
import { getGames, getGameScores } from "../mars-api";
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
      pickedGame: {},
      GAME_SCHEMA: {
        Id: "id",
        "Player #": "player_count",
        "Date": "date",
        "Map": "game_map",
        "Gen #": "number_of_generations",
        "Draft": "draft",
        "Prelude": "prelude",
        "Venus Next": "venus_next",
        "Colonies": "colonies",
      },
      tableSortParams: {
        ascending: false,
        sortColumn: "",
      },
    };
  },
  methods: {
    getOrderByName() {
      return this.orderByDirection + this.orderByName;
    },
    fetchGames(order_by = this.getOrderByName()) {
        order_by = this.getOrderByName()
      getGames(this.limit, this.currentOffset, order_by)
        .then((response) => {
          this.totalNumberOfGames = response.data.count;
          this.games = response.data.results;
        })
        .then(() => console.log(this.games))
        .catch((error) => console.log(error));
    },
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
    fetchGameScores(id) {
      console.log("fetchGameScores");
      getGameScores(id)
        .then((response) => {
          this.pickedGame = response.data;
          console.log(response.data);
        })
        .catch((error) => console.log("error"));
    },
  },
  created: function () {
    console.log("created hook");
  },
  mounted: function () {
    this.fetchGames();
  },
  computed: {
    isPreviousDisabled() {
      if (this.currentOffset >= this.limit) return null;
      // Vue 3 ..
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


<style lang="scss" module scoped>
th {
cursor: pointer;
}
th:hover {
background-color: lavender;
}
</style>
