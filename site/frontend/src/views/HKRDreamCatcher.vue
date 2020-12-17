<template>
  <div>
    <div v-if="!spoilerRetrieved">
      <v-row>
        <v-col cols="12" sm="8" offset-sm="2">
          <h2>Hollow Knight Randomizer "Quick Seed" Tool</h2>
          <p>This tool allows for a "quick play" seed by showing the location of important items and abilities. You may customize what is shown below with "Show Item Options".</p>

          <p>Thanks to BearsAndBeets for design and color help and the Sneakbike Community for various ideas and improvements.</p>

          <hr />
          <br />
          <h2>Quickstart</h2>
          <p>
            <b>Pick what things you want displayed in "Show Item Options". Then upload your Hollow Knight Randomizer Spoiler below. This is usually located (on Windows) at:</b>
          </p>

          <p>
            <code>C:\Users\yourname\AppData\LocalLow\Team Cherry\Hollow Knight\RandomizerSpoilerLog.txt</code>
          </p>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" sm="8" offset-sm="2">
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header>Show Item Options</v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-switch v-model="showDreamers" :label="'Show Dreamers?'" />
                <v-switch v-model="showAbilities" :label="'Show Abilities?'" />
                <v-switch v-model="showUsefulItems" :label="'Show Useful Items?'" />
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
          <v-btn :disabled="spoiler_txt.length === 0" @click="parseWithAPI">Submit</v-btn>
        </v-col>
      </v-row>
    </div>

    <div v-if="spoilerRetrieved">
      <v-row>
        <v-col cols="12" sm="8" offset-sm="2">
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header>Show Item Options</v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-switch v-model="showDreamers" :label="'Show Dreamers?'" />
                <v-switch v-model="showAbilities" :label="'Show Abilities?'" />
                <v-switch v-model="showUsefulItems" :label="'Show Useful Items?'" />
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-col>
      </v-row>
      <v-col cols="12" sm="8" offset-sm="2">
        <HKRItemTable :dataToShow="dataToShow" />
      </v-col>
      <br />
      <br />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import HKRItemTable from "@/components/HollowKnight/HKRItemTable.vue";

export default {
  name: "HKRDreamCatcher",
  components: { HKRItemTable },
  data: function () {
    return {
      spoiler_txt: "",
      spoilerRetrieved: false,
      showDreamers: true,
      showAbilities: true,
      showUsefulItems: false,
      arrayDreamers: () => [],
      arrayAbilities: () => [],
      arrayUsefulItems: () => [],
    };
  },
  computed: {
    dataToShow() {
      var arraysToConcat = [];
      if (this.showDreamers) {
        arraysToConcat.push(this.arrayDreamers);
      }
      if (this.showAbilities) {
        arraysToConcat.push(this.arrayAbilities);
      }
      if (this.showUsefulItems) {
        arraysToConcat.push(this.arrayUsefulItems);
      }
      const dataNotGrouped = [].concat(...arraysToConcat);
      const data = dataNotGrouped.reduce((result, item) => {
        if (result[item[0]]) {
          result[item[0]].push(item[1]);
        } else {
          result[item[0]] = [item[1]];
        }
        return result;
      }, {});
      const orderedData = Object.keys(data)
        .sort()
        .reduce(
          (result, item) => ((result[item] = data[item].sort()), result),
          {}
        );
      return orderedData;
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
          this.arrayAbilities = resp["abilities"];
          this.arrayUsefulItems = resp["useful_items"];

          this.spoilerRetrieved = true;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
