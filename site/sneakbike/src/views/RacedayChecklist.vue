<template>
  <div class="raceday-checklist">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <RaceChecklist />
        </v-col>
        <v-col cols="2" />
      </v-row>
    </v-container>
  </div>
</template>

<script>
import RaceChecklist from "@/components/RaceChecklist.vue";
export default {
  name: "RacedayChecklist",
  components: {
    RaceChecklist,
  },
};
</script>
