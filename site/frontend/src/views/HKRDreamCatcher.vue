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

    <div v-if="spoilerRetrieved">
      <v-col cols="12" sm="8" offset-sm="2">
        <table>
          <tr v-for="(itemList, loc, idx) in locationsOfItems" :key="`${loc}-${idx}`">
            <th>{{ loc }}</th>
            <td>
              <v-card class="d-flex flex-wrap item-wrapper" flat tile>
                <div v-for="(item, jdx) in itemList" :key="`${item}-${idx}-${jdx}`">
                  <tracker-image
                    :src="`assets/hollow_knight/${mapItemToBaseItem(parseImageName(item))}.png`"
                    :alt="`${item}`"
                    :height="48"
                    :width="48"
                  />
                </div>
              </v-card>
            </td>
          </tr>
        </table>
      </v-col>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import TrackerImage from "@/components/TrackerImage.vue";

// TODO: Maybe we can trim these item names and map them to the item picture.
const itemToImageMapping = {
  Mothwing_Cloak: "Shade_Cloak",
  Shade_Soul: "Vengeful_Spirit",
  Descending_Dark: "Desolate_Dive",
  Abyss_Shriek: "Howling_Wraiths",
};

export default {
  name: "HKRDreamCatcher",
  components: { TrackerImage },
  data: function () {
    return {
      spoiler_txt: "",
      spoilerRetrieved: false,
      locationsOfItems: () => {},
      numLocations: 0,
      itemToImageMapping,
    };
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
          this.locationsOfItems = resp.all_items_gb_loc;
          this.numLocations = Object.keys(this.locationsOfItems).length;
          this.panel = [...Array(this.numLocations).keys()];

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

.v-expansion-panel-content__wrap {
  padding: 0 !important;
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