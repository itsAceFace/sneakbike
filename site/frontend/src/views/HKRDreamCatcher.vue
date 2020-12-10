<template>
  <div>
    <div v-if="!spoilerRetrieved">
      <row>
        <v-col cols="12" sm="8" offset-sm="2">
          <h2>Hollow Knight Randomizer "Quick Seed" Tool</h2>
          <p>This tool allows for a "quick play" seed by showing the location of important items and abilities. You may customize what is shown below with "Show Item Options".</p>

          <p>
            <b>Upload your Hollow Knight Randomizer Spoiler below. This is usually located (on Windows) at:</b>
          </p>

          <p>
            <code>C:\Users\yourname\AppData\LocalLow\Team Cherry\Hollow Knight\RandomizerSpoilerLog.txt</code>
          </p>
        </v-col>
      </row>

      <v-row>
        <v-col cols="12" sm="8" offset-sm="2">
          <!-- TODO: DRY HERE -->
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header>Show Item Options</v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-switch v-model="showDreamers" :label="'Show Dreamers?'" />
                <v-switch v-model="showBasicAbilities" :label="'Show Basic Abilities?'" />
                <v-switch v-model="showAdvancedAbilities" :label="'Show Advanced Abilities?'" />
                <v-switch v-model="showStandardItems" :label="'Show Standard Items?'" />
                <v-switch v-model="showOtherKeys" :label="'Show Other Keys?'" />
                <v-switch v-model="showPaleOre" :label="'Pale Ore?'" />
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="6" offset-sm="2">
          <v-file-input
            truncate-length="120"
            accept=".txt"
            label="File input"
            @change="onFileChange"
          />
        </v-col>
        <v-col cols="2">
          <v-btn v-if="spoiler_txt" @click="parseWithAPI">Submit</v-btn>
        </v-col>
      </v-row>
    </div>

    <div v-else>
      <v-row>
        <v-col>
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header>Show Item Options</v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-switch v-model="showDreamers" :label="'Show Dreamers?'" />
                <v-switch v-model="showBasicAbilities" :label="'Show Basic Abilities?'" />
                <v-switch v-model="showAdvancedAbilities" :label="'Show Advanced Abilities?'" />
                <v-switch v-model="showStandardItems" :label="'Show Standard Items?'" />
                <v-switch v-model="showOtherKeys" :label="'Show Other Keys?'" />
                <v-switch v-model="showPaleOre" :label="'Pale Ore?'" />
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-col>
      </v-row>

      <v-data-table
        dense
        hide-default-footer
        disable-pagination
        item-key="item"
        show-select
        :headers="tableHeaders"
        :items="spoilersList"
        :mobile-breakpoint="200"
        class="elevation-1"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HKRDreamCatcher",
  data: function () {
    return {
      spoiler_txt: "",
      spoilerRetrieved: false,
      locsDreamers: () => [],
      locsBasicAbilities: () => [],
      locsAdvancedAbilities: () => [],
      locsStandardItems: () => [],
      locsOtherKeys: () => [],
      locsPaleOre: () => [],
      showDreamers: true,
      showBasicAbilities: true,
      showAdvancedAbilities: false,
      showStandardItems: false,
      showOtherKeys: false,
      showPaleOre: false,
      tableHeaders: [
        { text: "Item", align: "start", sortable: true, value: "item" },
        { text: "Location", align: "start", sortable: true, value: "location" },
      ],
      selectedRows: [],
    };
  },
  computed: {
    spoilersList() {
      var arraysToConcat = [];

      if (this.showDreamers) {
        arraysToConcat.push(this.locsDreamers);
      }
      if (this.showBasicAbilities) {
        arraysToConcat.push(this.locsBasicAbilities);
      }
      if (this.showAdvancedAbilities) {
        arraysToConcat.push(this.locsAdvancedAbilities);
      }
      if (this.showStandardItems) {
        arraysToConcat.push(this.locsStandardItems);
      }
      if (this.showOtherKeys) {
        arraysToConcat.push(this.locsOtherKeys);
      }
      if (this.showPaleOre) {
        arraysToConcat.push(this.locsPaleOre);
      }

      return [].concat(...arraysToConcat);
    },
  },
  methods: {
    onFileChange(file) {
      if (!(file.size || file.name === "RandomizerSpoilerLog.txt")) return;
      this.createText(file);
    },
    createText(file) {
      var reader = new FileReader();
      reader.readAsText(file);
      reader.onload = (e) => {
        this.spoiler_txt = e.target.result;
      };
    },
    parseWithAPI() {
      axios
        .post(`${process.env.VUE_APP_API_LOCATION}/hkr/uploadspoiler/`, {
          files: this.spoiler_txt,
        })
        .then((response) => {
          const resp = response["data"];
          this.locsDreamers = resp.dreamers;
          this.locsBasicAbilities = resp.basic_abilities;
          this.locsAdvancedAbilities = resp.advanced_abilities;
          this.locsStandardItems = resp.standard_items;
          this.locsOtherKeys = resp.other_keys;
          this.locsPaleOre = resp.pale_ore;

          this.spoilerRetrieved = true;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

<style>
th.text-start {
  background-color: #9cccff !important;
}
.v-input--selection-controls {
  margin-top: 0 !important;
  padding-top: 0 !important;
}
</style>