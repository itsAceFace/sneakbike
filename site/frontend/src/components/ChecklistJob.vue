<template>
  <div class="job">
    <br />
    <v-progress-linear v-model="progressVal" color="blue" />
    <br />
    <div
      v-for="(dutyList, timeSection, index) in dutiesJOB"
      :key="`dutiesJOB-${index}`"
    >
      <div class="time-section">
        <span class="time-section">{{ timeSection }}</span>
      </div>
      <div
        v-for="(duty, index2) in dutyList"
        :key="`dutiesJOB-dutyList-${timeSection}-${index}-${index2}`"
      >
        <v-checkbox
          v-model="selected"
          :value="`dutiesJOB-dutyList-${index}-${index2}`"
        >
          <template v-slot:label>
            <span class="checklist-item">{{ duty }}</span>
          </template>
        </v-checkbox>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ChecklistJob",
  data() {
    return { selected: [] };
  },
  props: {
    dutiesJOB: Object,
  },
  computed: {
    progressVal() {
      return (
        (100.0 * this.selected.length) /
        (1.0 * Object.values(this.dutiesJOB).flat().length)
      );
    },
  },
  created() {
    this.selected = [];
  },
};
</script>

<style lang="scss" scoped>
.v-input--selection-controls {
  margin-top: 0 !important;
  padding-top: 0 !important;
  margin-bottom: 0 !important;
  padding-bottom: 0 !important;
}

span.time-section {
  font-weight: bold;
}
div.time-section {
  margin-bottom: 1rem !important;
}
</style>
