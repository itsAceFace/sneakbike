<template>
  <div>
    <v-row>
      <v-col cols="12" sm="8" offset-sm="2">
        
        <div v-if="Object.keys(spoilers).length === 0">
          <v-file-input
            truncate-length="120"
            accept=".txt"
            label="File input"
            @change="onFileChange"
          />
          <v-btn v-if="spoiler_txt" @click="parseWithAPI">Submit</v-btn>
        </div>

        <div v-else>
          <v-card>
            <v-card-title>
              <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                single-line
                hide-details
              />
            </v-card-title>
            <v-data-table
              dense
              :headers="tableHeaders"
              :items="spoilers"
              item-key="spoiler"
              hide-default-footer
              :items-per-page="1000"
              :mobile-breakpoint="200"
              class="elevation-1"
            />
          </v-card>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HKRDreamCatcher",
  data: function () {
    return {
      spoiler_txt: "",
      dreamers: "",
      keyItems: "",
      tableHeaders: [{text: 'Item', align: 'start', sortable: true, value: 'item'}, {text: 'Location', align: 'start', sortable: true, value: 'location'}],
      search: ""
    };
  },
  computed: {
    spoilers() {
      return this.dreamers.concat(this.keyItems);
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
    console.log(`${process.env.VUE_APP_API_LOCATION}`)
      axios
        .post(`${process.env.VUE_APP_API_LOCATION}/hkr/uploadspoiler/`, {
          files: this.spoiler_txt,
        })
        .then((response) => {
          const resp = response["data"];
          this.dreamers = resp.dreamers;
          this.keyItems = resp.key_items;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
