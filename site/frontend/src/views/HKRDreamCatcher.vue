<template>
  <div>
    <div v-if="!spoilerRetrieved">
      <v-row>
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
      </v-row>
    </div>
    <div>
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
          <v-btn :disabled="spoiler_txt.length === 0" @click="parseWithAPI">Submit</v-btn>
        </v-col>
      </v-row>
    </div>
    <div>
      <v-row>
        <v-col cols="12" sm="8" offset-sm="2">
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header>Show Item Options</v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-switch v-model="showDreamers" :label="'Show Dreamers?'" />
                <v-switch v-model="showMainAbilities" :label="'Show Main Abilities?'" />
                <v-switch v-model="showAdvancedAbilities" :label="'Show Advanced Abilities?'" />
                <v-switch v-model="showUsefulItems" :label="'Show Useful Items?'" />
                <v-switch v-model="showOtherUsefulItems" :label="'Show Other Useful Items?'" />
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-col>
      </v-row>
    </div>
    <div v-if="spoilerRetrieved">
      <v-col cols="12" sm="8" offset-sm="2">
        <HKRItemTable :dataToShow="dataToShow" />
      </v-col>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { reduce } from "lodash";
import HKRItemTable from "@/components/HKRItemTable.vue";

export default {
  name: "HKRDreamCatcher",
  components: { HKRItemTable },
  data: function () {
    return {
      spoiler_txt: "",
      spoilerRetrieved: false,
      showDreamers: true,
      showMainAbilities: true,
      showAdvancedAbilities: false,
      showUsefulItems: false,
      showOtherUsefulItems: false,
      arrayDreamers: () => [],
      arrayMainAbilities: () => [],
      arrayAdvancedAbilities: () => [],
      arrayUsefulItems: () => [],
      arrayOtherUsefulItems: () => [],
    };
  },
  computed: {
    dataToShow() {
      var arraysToConcat = [];
      if (this.showDreamers) {
        arraysToConcat.push(this.arrayDreamers);
      }
      if (this.showMainAbilities) {
        arraysToConcat.push(this.arrayMainAbilities);
      }
      if (this.showAdvancedAbilities) {
        arraysToConcat.push(this.arrayAdvancedAbilities);
      }
      if (this.showUsefulItems) {
        arraysToConcat.push(this.arrayUsefulItems);
      }
      if (this.showOtherUsefulItems) {
        arraysToConcat.push(this.arrayOtherUsefulItems);
      }
      const dataNotGrouped = [].concat(...arraysToConcat);
      // const data = groupBy(dataNotGrouped, (s) => s[0]);
      const data = reduce(
        dataNotGrouped,
        function (result, item) {
          if (result[item[0]]) {
            result[item[0]].push(item[1]);
          } else {
            result[item[0]] = [item[1]];
          }
          return result;
        },
        {}
      );
      return data;
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
          this.arrayDreamers = resp["dreamers"];
          this.arrayMainAbilities = resp["main_abilities"];
          this.arrayAdvancedAbilities = resp["advanced_abilities"];
          this.arrayUsefulItems = resp["useful_items"];
          this.arrayOtherUsefulItems = resp["other_useful_items"];

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

.v-expansion-panel--active > .v-expansion-panel-header {
  min-height: 0 !important;
}

td,
th {
  border: 1px solid #ccc;
  text-align: center;
  border-color: rgba(0, 0, 0, 0.15);
}
th {
  background: #669ede;
  border-color: white;
  padding-left: 1rem;
  padding-right: 1rem;
}

.item-wrapper {
  margin-bottom: 0 !important;
  padding-left: 0.5rem !important;
  padding-right: 0.5rem !important;
  background: #5f5f5f !important;
}
</style>