<template>
<!--
  <section class="hero is-primary">
    <div class="hero-body">
      <div class="container">
        <h1 class="title">
          TM Stats
          <span class="icon">
            <i class="fas fa-meteor"></i>
          </span>
        </h1>
        <p class="title is-3">Terraforming Mars board game statistics</p>
        <p class="subtitle is-5">
          <button class="button is-link is-light" onclick="window.location.href='/mars_api/'">API</button>
        </p>
      </div>
    </div>
  </section>
-->
<NavBar> </NavBar>


  <div class="tile is-ancestor">
    <div class="tile is-6 is-vertical is-parent">
      <div class="tile is-child box has-text-centered">
        <button class="button is-primary">Add Game</button>
      </div>
      <div class="tile is-child box">
        <h3 class="title">Player stats</h3>
      </div>
    </div>
    <div class="tile is-parent">
      <div class="tile is-child box">
        <h3 class="title">Recent games</h3>
      </div>
    </div>
  </div>
  <Game></Game>
</template>



<script lang="ts">
import NavBar from "./components/NavBar.vue";
import Game from "./components/Game.vue";
export default {
  components: {
    NavBar,
    Game,
  },
};
</script>
