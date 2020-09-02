<template>
  <div class="score">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <h1>Scoreboard</h1>
          <ScoreBoardComponent :runnerScores="runnerScores" />
        </v-col>
        <v-col cols="2" />
      </v-row>
    </v-container>
  </div>
</template>

<script>
import ScoreBoardComponent from "@/components/ScoreBoardComponent.vue";
import runnerScores from "@/data/runnerScores.js";

export default {
  name: "Team",
  data() {
    return {
      runnerScores,
    };
  },
  components: { ScoreBoardComponent },
};
</script>
