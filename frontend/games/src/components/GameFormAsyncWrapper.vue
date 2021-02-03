<template>
  <GameForm :game="game" :MAPS="MAPS"/>
</template>


<script>
import GameForm from "./GameForm";
import { getMaps } from "../mars-api";

export default {
  props: {
    game: {
      type: Object,
      required: true,
    },
  },
  components: {
    GameForm,
  },
  async setup() {
    const {data: MAPS} = await getMaps();
    return {
      MAPS,
    };
  },
};
</script>
