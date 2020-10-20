<template>
  <div class="table-container">

    <table class="table is-hoverable" v-if="gameId">
      <thead>
        <th>-/-</th>
        <th v-for="player in this.pivotedGameScores.player">{{player.nickname}}</th>
      </thead>
      <tbody>
        <tr v-for="(displayName, modelName) in this.PLAYER_SCORE_FIELDS_TO_DISPLAY">
          <td>{{displayName}}</td>
          <td
            v-for="value in
          this.pivotedGameScores[modelName]"
          >{{displayPlayerScoreProperty(value, modelName)}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { Vue, ref, toRefs, watch } from "vue";
import { PLAYER_SCORE_SCHEMA, getGameScores } from "../mars-api";
import lodash from "lodash";

export default {
  props: { gameId: Number },
  setup(props) {
    const { gameId } = toRefs(props);
    const gameScores = ref({});
    const pivotedGameScores = ref({});

    const fetchGameScores = async (gameId) => {
      await getGameScores(gameId).then(
        (response) => (gameScores.value = response.data)
      );
    };

    const pivotGameScores = () => {
      pivotedGameScores.value = {};
      for (let property in PLAYER_SCORE_SCHEMA) {
        pivotedGameScores.value[property] = [];
      }

      for (let score of gameScores.value.scores) {
        for (let prop in score) {
          pivotedGameScores.value[prop].push(score[prop]);
        }
      }
    };

    const updateGameScores = async (gameId) => {
      if (gameId) {
        await fetchGameScores(gameId);
        pivotGameScores();
      }
    };
    watch(gameId, updateGameScores);

    let PLAYER_SCORE_FIELDS_TO_DISPLAY = lodash.cloneDeep(PLAYER_SCORE_SCHEMA);
    delete PLAYER_SCORE_FIELDS_TO_DISPLAY.game_id;
    delete PLAYER_SCORE_FIELDS_TO_DISPLAY.id;

    return {
      gameScores,
      pivotedGameScores,
      fetchGameScores,
      PLAYER_SCORE_FIELDS_TO_DISPLAY,
    };
  },
  data() {
    return {
      PLAYER_SCORE_SCHEMA: PLAYER_SCORE_SCHEMA,
    };
  },
  methods: {
    displayPlayerScoreProperty(prop, modelName) {
      if (modelName === "player") {
        return prop.nickname;
      }
      if (modelName === "is_winner") {
        return prop ? "Yes" : "No";
      } else return prop;
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
