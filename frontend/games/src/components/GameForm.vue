<template>
  <div class="card">
    <div class="card-content">
      <div class="level">
        <div class="level-item">
          <BaseDate v-model="game.date" label="date" />
        </div>
        <div class="level-item">
          <BaseNumberInput
            v-model.number="game.number_of_generations"
            label="number of generations"
            type="number"
          />
        </div>
        <div class="level-item">
          <BaseSelect v-model="game.game_map" label="Map" :options="MAPS" />
        </div>

        <div class="level-item">
          <BaseCheckbox v-model="game.draft_variant" label="Draft?" />
        </div>

        <div class="level-item">
          <BaseCheckbox v-model="game.prelude" label="Prelude?" />
        </div>
        <div class="level-item">
          <BaseCheckbox v-model="game.colonies" label="Colonies?" />
        </div>
        <div class="level-item">
          <BaseCheckbox v-model="game.venus_next" label="Venus Next?" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    game: {
      type: Object,
      required: true,
    },
    MAPS: {
      type: Array,
      required: true,
    },
  },
};
</script>
