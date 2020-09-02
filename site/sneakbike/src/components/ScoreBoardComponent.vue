<template>
  <div class="scoreboardcomponent">
    <v-data-table
      :headers="headers"
      :items="runnerScores"
      hide-default-footer
      :items-per-page="500"
      class="elevation-1"
    />
  </div>
</template>

<script>
const headers = [
  {
    text: "Runner",
    align: "start",
    sortable: true,
    value: "runner",
  },
  { text: "Total Races", value: "totalRaces" },
  { text: "Level", value: "level" },
  { text: "Points", value: "points" },
  {
    text: "Relative Points",
    value: "relativePoints",
  },
];

export default {
  name: "ScoreBoardComponent",
  props: { runnerScores: Object },
  data() {
    return {
      headers,
    };
  },
};
</script>