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
    </div>
    <div v-if="spoilerRetrieved">
      <v-col cols="12" sm="8" offset-sm="2">
        <HKRItemTable
          :locationOfItems="locationOfItems"
          :itemsToShow="itemsToShow"
          :locationsToShow="locationsToShow"
        />
      </v-col>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import { intersection } from "lodash";
import HKRItemTable from "@/components/HKRItemTable.vue";

const arrayDreamers = ["Herrah", "Monomon", "Lurien", "Dreamer"];
const arrayBasicAbilities = [
  "Vengeful_Spirit",
  "Desolate_Dive",
  "Ismas_Tear",
  "Mothwing_Cloak",
  "Crystal_Heart",
  "Mantis_Claw",
  "Dream_Nail",
  "Monarch_Wings",
];
const arrayAdvancedAbilities = [
  "Abyss_Shriek",
  "Shade_Soul",
  "Howling_Wraiths",
  "Shade_Cloak",
  "Dream_Gate",
  "Awoken_Dream_Nail",
  "Great_Slash",
  "Descending_Dark",
];
const arrayStandardItems = ["Lumafly_Lantern", "Simple_Key", "Grimmchild"];
const arrayOtherKeys = [
  "Elegant_Key",
  "Kings_Brand",
  "Shopkeepers Key",
  "City_Crest",
  "Tram_Pass",
  "Love_Key",
];
const arrayPaleOre = ["Pale_Ore"];

const itemToImageMapping = {
  Mothwing_Cloak: "Shade_Cloak",
  Shade_Soul: "Vengeful_Spirit",
  Descending_Dark: "Desolate_Dive",
  Abyss_Shriek: "Howling_Wraiths",
  Awoken_Dream_Nail: "Dream_Nail",
  Dream_Gate: "Dream_Gate",
};

export default {
  name: "HKRDreamCatcher",
  components: { HKRItemTable },
  data: function () {
    return {
      spoiler_txt: "",
      spoilerRetrieved: false,
      showDreamers: true,
      showBasicAbilities: true,
      showAdvancedAbilities: false,
      showStandardItems: false,
      showOtherKeys: false,
      showPaleOre: false,
      locationOfItems: () => {},
      arrayStandardItems,
      arrayOtherKeys,
      arrayPaleOre,
      arrayDreamers,
      arrayBasicAbilities,
      arrayAdvancedAbilities,
      itemToImageMapping,
    };
  },
  computed: {
    itemsToShow() {
      var arraysToConcat = [];
      if (this.showDreamers) {
        arraysToConcat.push(this.arrayDreamers);
      }
      if (this.showBasicAbilities) {
        arraysToConcat.push(this.arrayBasicAbilities);
      }
      if (this.showAdvancedAbilities) {
        arraysToConcat.push(this.arrayAdvancedAbilities);
      }
      if (this.showStandardItems) {
        arraysToConcat.push(this.arrayStandardItems);
      }
      if (this.showOtherKeys) {
        arraysToConcat.push(this.arrayOtherKeys);
      }
      if (this.showPaleOre) {
        arraysToConcat.push(this.arrayPaleOre);
      }
      return [].concat(...arraysToConcat);
    },
    locationsToShow() {
      const locs = Object.keys(this.locationOfItems);
      const locsToShow = [];

      for (var idx = 0; idx < locs.length; idx++) {
        let parsedItems = this.locationOfItems[locs[idx]].map((item) =>
          this.mapItemToBaseItem(this.parseImageName(item))
        );
        if (intersection(this.itemsToShow, parsedItems).length > 0) {
          locsToShow.push(locs[idx]);
        }
      }
      return locsToShow;
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
          this.locationOfItems = resp.all_items_gb_general_loc;

          this.spoilerRetrieved = true;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    mapItemToBaseItem(itemName) {
      if (Object.keys(itemToImageMapping).includes(itemName)) {
        return itemToImageMapping[itemName];
      } else {
        return itemName;
      }
    },
    parseImageName(itemName) {
      itemName = itemName.replace(/['\\]/g, "");
      itemName = itemName.replace(/ /g, "_");
      itemName = itemName.replace(/-.*/g, "");
      return itemName;
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
  background: rgb(227, 240, 255);
  border-color: white;
  padding-left: 1rem;
  padding-right: 1rem;
}

.item-wrapper {
  margin-bottom: 0 !important;
  padding-left: 0.5rem !important;
  padding-right: 0.5rem !important;
  background: rgb(249, 249, 249) !important;
}
</style>