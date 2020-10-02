<template>
  <div class="tile is-ancestor">
    <div class="tile is-5 is-vertical is-parent">
      <div class="tile is-child pagination is-centered">
        <a class="pagination-previous" v-on:click="this.navigateGames(false)"
        v-bind:disabled="isPreviousDisabled">Previous</a>
        <a class="pagination-next" v-on:click="this.navigateGames(true)"
        v-bind:disabled="isNextDisabled">Next</a>
      </div>

      <div class="table-container is-child box">
        <table class="table is-striped is-hoverable">
          <thead>
            <tr>
              <th>Id</th>
              <th>Date</th>
              <th>Game Map</th>
              <th>Num Of Gen</th>
              <th>Draft</th>
              <th>Prelude</th>
              <th>Venus Next</th>
              <th>Colonies</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="game in games" v-bind:key="game">
              <td v-for="(value, key) in game" v-bind:key="key">{{ value }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="tile is-vertical is-parent">
      <div class="tile box is-child">
        <h1 class="title">Game Details</h1>
        <p>Select a game from the list..</p>
      </div>
    </div>
  </div>
</template>

<script>
import { getAllGames } from "../mars-api";
let limit = 50;
let currentoffset = 0;

export default {
  data() {
    return {
      games: [],
      limit: 50,
      currentOffset: 0,
      totalNumberOfGames: 0,
    };
  },
  methods: {
    fetchGames() {
      getAllGames(this.limit, this.currentOffset)
        .then((response) => {
          this.totalNumberOfGames = response.data.count;
          console.log(this.totalNumberOfGames);
          this.games = response.data.results;
        })
        .then(() => console.log(this.games))
        .catch((error) => console.log(error));
    },
    navigateGames(forward) {
        if (forward){
            if(this.currentOffset + this.limit < this.totalNumberOfGames)
                this.currentOffset += this.limit;
        }
      else {
        if (this.currentOffset <= this.limit) this.currentOffset = 0;
        else this.currentOffset -= this.limit;
      }
      this.fetchGames();
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
        if (this.currentOffset >= this.limit)
            return null; // Vue 3 ..
        else return true;
    },
    isNextDisabled() {
        if(this.currentOffset + this.limit < this.totalNumberOfGames)
            return null;
        else return true;
    }
}
};
</script>

