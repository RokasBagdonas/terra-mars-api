<template>
  <h5>player score form</h5>
  <p>{{ playerScore}}</p>

  <BaseInput v-model="playerScore.terraform_rating" label="TR" type="number"/>
</template>


<script lang="ts">
import BaseInput from "./form-components/BaseInput.vue";
import { PlayerScore } from "../classes";
import { PropType } from "vue";

export default {
  components: {
    BaseInput,
  },
  props: {
    playerScore: {
      type: Object,
      required: true,
    },
  },
};
</script>
