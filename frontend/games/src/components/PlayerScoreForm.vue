<template>
<!--
  <div class="card">
  <div class="card-header">
  -->
    <BaseObjectSelect
      v-model="playerScore.player"
      label="Player"
      :options="PLAYERS"
      displayProp="nickname"
    />
    <BaseSelect
      v-model="playerScore.corporation"
      label="corporation"
      :options="CORPORATIONS"
    />
    <BaseCheckbox v-model="playerScore.is_winner" label="Won?" />
    <!--
  </div>
  -->
  <!--
  <div class="card-content">
  -->
    <div class="hero is-small is-primary">
      <div class="hero-body">
        <p>Total Score: {{ totalScore }}</p>
      </div>
    </div>
    <BaseNumberInput
      v-model.number="playerScore['terraform_rating']"
      label="TR"
      type="number"
    />
    <BaseNumberInput
      v-model.number="playerScore.milestones"
      label="Milestones"
      type="number"
    />
    <BaseNumberInput
      v-model.number="playerScore.awards"
      label="Awards"
      type="number"
    />
    <BaseNumberInput
      v-model.number="playerScore.greeneries"
      label="Greeneries"
      type="number"
    />
    <BaseNumberInput
      v-model.number="playerScore.cities"
      label="Cities"
      type="number"
    />
    <BaseNumberInput
      v-model.number="playerScore.event_cards"
      label="Events"
      type="number"
    />
    <BaseNumberInput
      v-model.number="playerScore.automated_cards"
      label="Automated Cards"
      type="number"
    />
    <BaseNumberInput
      v-model.number="playerScore.active_cards"
      label="Active cards"
      type="number"
    />
    <BaseNumberInput
      v-model.number="playerScore.resources"
      label="Resources"
      type="number"
    />
    <!--
</div>
  </div>
  -->
</template>


<script>
export default {
  props: {
    playerScore: {
      type: Object,
      required: true,
    },
    CORPORATIONS: {
      type: Array,
      required: true,
    },
    PLAYERS: {
      type: Array,
      required: true,
    },
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
