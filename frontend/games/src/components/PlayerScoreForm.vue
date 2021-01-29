<template>
  <div class="container">
    <p>{{ playerScore }}</p>

    <BaseSelect
      v-model="playerScore.corporation"
      label="corporation"
      :options="corporations"
    />
    <BaseInput
      v-model.number="playerScore['terraform_rating']"
      label="TR"
      type="number"
    />
    <BaseInput
      v-model.number="playerScore.milestones"
      label="Milestones"
      type="number"
    />
    <BaseInput v-model.number="playerScore.awards" label="Awards" type="number" />
    <BaseInput
      v-model.number="playerScore.greeneries"
      label="Greeneries"
      type="number"
    />
    <BaseInput v-model.number="playerScore.cities" label="Cities" type="number" />
    <BaseInput v-model.number="playerScore.event_cards" label="Events" type="number" />
    <BaseInput
      v-model.number="playerScore.automated_cards"
      label="Automated Cards"
      type="number"
    />
    <BaseInput
      v-model.number="playerScore.active_cards"
      label="Active cards"
      type="number"
    />
    <BaseInput
      v-model.number="playerScore.resources"
      label="Resources"
      type="number"
    />
    <BaseInput v-model.number="playerScore.total_score" label="total" type="number" />
    <BaseInput v-model="playerScore.is_winner" label="Won?" type="string" />
  </div>
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
      PlayerScore,
    };
  },
};
</script>
