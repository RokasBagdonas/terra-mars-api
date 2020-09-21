<template>
<div class="tile is-ancestor">
  <div class="tile is-4 is-vertical is-parent">
    <div class="tile is-child box">
      <p class="title">One</p>
    </div>
    <div class="tile is-child box">
      <p class="title">Two</p>
    </div>
  </div>
  <div class="tile is-parent">
    <div class="tile is-child box">
      <p class="title">Three</p>
    </div>
  </div>
</div>
<!--
    </div>
  <div class="container">
    <img src="./assets/mars-144.png" />
    <HelloWorld msg="Terraforming Mars game statistics" />
  </div>
  -->

</template>


<script>
import HelloWorld from "./components/HelloWorld.vue";

export default {
  name: "App",
  components: {
    HelloWorld,
  },
};
</script>
