<template>
  <nav class="navbar is-primary" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
        <h1 class="navbar-item title is-3">
            <i class="icon fas fa-meteor"></i>
        </h1>
        <a role="button" class="navbar-burger" aria-label="menu"
        aria-expanded="false" data-target="navbarOptions" v-on:click="toggleBurger">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
        </a>
    </div>
    <div class="navbar-menu" id="navbarOptions">
        <div class="navbar-start">
            <a class="navbar-item" href="/mars_api">Home</a>
            <a class="navbar-item" href="">Add Game</a>
            <a class="navbar-item" href="">Games</a>
            <a class="navbar-item" href="">Player Stats</a>
            <a class="navbar-item" href="">About</a>
        </div>
    </div>
  </nav>
</template>

<script lang="ts">
/*import Vue from 'vue'*/
/*export default Vue.extend({*/

/*})*/
export default {
methods: {
    toggleBurger: function(event) {
        const navbarTarget = event.target.dataset.target;
        const elTarget = document.getElementById(navbarTarget);

        if (elTarget != null) {
            event.target.classList.toggle("is-active");
            elTarget.classList.toggle("is-active");
        }
        else console.error("Couldn't find navbar element.");
    }
 }
};
</script>
