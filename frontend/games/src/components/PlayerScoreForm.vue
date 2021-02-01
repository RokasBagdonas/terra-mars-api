<template>
  <div class="container">
    <h3>Total score: {{ totalScore }}</h3>

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
    <BaseInput
      v-model.number="playerScore.awards"
      label="Awards"
      type="number"
    />
    <BaseInput
      v-model.number="playerScore.greeneries"
      label="Greeneries"
      type="number"
    />
    <BaseInput
      v-model.number="playerScore.cities"
      label="Cities"
      type="number"
    />
    <BaseInput
      v-model.number="playerScore.event_cards"
      label="Events"
      type="number"
    />
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
    <BaseCheckbox v-model="playerScore.is_winner" label="Won?"/>
  </div>
</template>


<script>
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
  computed: {
    totalScore() {
      let total =
        this.playerScore.terraform_rating +
        this.playerScore.milestones +
        this.playerScore.awards +
        this.playerScore.greeneries +
        this.playerScore.cities +
        this.playerScore.event_cards +
        this.playerScore.automated_cards +
        this.playerScore.active_cards +
        this.playerScore.resources;
      return total;
    },
  },
};
</script>
