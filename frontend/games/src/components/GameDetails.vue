<template>
  <div class="box">
    <div class="columns is-0" v-if="gameId">
      <div class="column">
        <div class="table-container">
          <table class="table is-hoverable">
            <tbody>
              <tr v-for="(displayName, modelName) in this.PLAYER_SCORE_FIELDS_TO_DISPLAY"
              :key="displayName">
                <td>{{displayName}}</td>
                <td
                  v-for="(value, index) in
          this.pivotedGameScores[modelName]" :key="index"
                >{{displayPlayerScoreProperty(value, modelName)}}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="column">
        <div class="table-container">
          <table class="table is-hoverable">
            <tr v-for="(value, name, index) in game" :key="index">
              <td>{{name}}</td>
              <td>{{value}}</td>
            </tr>
          </table>
        </div>
      </div>
    </div>
    <p v-else>👈 Click on one of the games to see more info</p>
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
    const game = ref({});

    const getGameData = () => {
      //Deep copy without scores.
      for (let prop in gameScores.value) {
        if (prop !== "scores") {
          game.value[prop] = gameScores.value[prop];
        }
      }
    };

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
        getGameData();
      }
    };

    watch(gameId, updateGameScores);

    let PLAYER_SCORE_FIELDS_TO_DISPLAY = lodash.cloneDeep(PLAYER_SCORE_SCHEMA);
    delete PLAYER_SCORE_FIELDS_TO_DISPLAY.game_id;
    delete PLAYER_SCORE_FIELDS_TO_DISPLAY.id;

    return {
      game,
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
