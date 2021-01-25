<template>
  <h5>player score form</h5>
  <p>{{ playerScore }}</p>
  <BaseInput v-model="playerScore.terraform_rating" label="TR" type="number" />
  <BaseSelect
    v-model="playerScore.corporation"
    label="corporation"
    type="string"
    :options="corporations"
  />
</template>


<script lang="ts">
import { PlayerScore } from "../classes";
import { ref } from "vue";

export default {
  props: {
    playerScore: {
      type: Object,
      required: true,
    },
  },
  setup() {
    let corporations = ["Tharsis Republic", "Teractor", "Saturn Systems"];
    return {
      corporations,
    };
  },
};
</script>
