<template>
  <h3 class="title is-3">GameForm</h3>
  <BaseSelect v-model="game.game_map" label="map" :options="MAPS"/>
 <BaseInput v-model.number="game.number_of_generations" label="number of generations"
 type="number"/>
 <BaseCheckbox v-model="game.draft_variant" label="Draft?"/>
 <BaseCheckbox v-model="game.prelude" label="Prelude?"/>
 <BaseCheckbox v-model="game.colonies" label="Colonies?"/>
 <BaseCheckbox v-model="game.venus_next" label="Venus Next?"/>
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
