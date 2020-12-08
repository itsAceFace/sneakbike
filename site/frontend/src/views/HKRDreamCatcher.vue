<template>
  <div>
    <v-row>
      <v-col cols="12" sm="8" offset-sm="2">
        <div v-if="!spoilerRetrieved">
          <v-file-input
            truncate-length="120"
            accept=".txt"
            label="File input"
            @change="onFileChange"
          />
          <v-btn v-if="spoiler_txt" @click="parseWithAPI">Submit</v-btn>
        </div>

        <div v-else>
          <v-row>
            <v-col>
              <v-switch
                v-model="switchDreamers"
                :label="'Dreamers?'"
              />
              <v-switch
                v-model="switchKeyItems"
                :label="'Major Items?'"
              />
            </v-col>
            <v-col></v-col>
          </v-row>

          <v-data-table
            dense
            hide-default-footer
            disable-pagination
            item-key="item"
            :headers="tableHeaders"
            :items="spoilersList"
            :mobile-breakpoint="200"
            class="elevation-1"
          >
            <template v-slot:body>
              <tbody>
                <tr :class="selectedRows.includes(k) ? 'selected-row' : ''" @click="rowSelect(k)" v-for="(v, k) in spoilersList" :key="v.item">
                  <td>{{ v.item }}</td>
                  <td>{{ v.location }}</td>
                </tr>
              </tbody>
            </template>
          </v-data-table>
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
      spoilerRetrieved: false,
      dreamers: "",
      keyItems: "",
      tableHeaders: [{text: 'Item', align: 'start', sortable: true, value: 'item'}, {text: 'Location', align: 'start', sortable: true, value: 'location'}],
      search: "",
      selectedRows: [],
      switchDreamers: true,
      switchKeyItems: false
    };
  },
  computed: {
    spoilersList() {
      var arraysToConcat = []
      if (this.switchDreamers) {
        arraysToConcat.push(this.dreamers)
      }
      if (this.switchKeyItems) {
        arraysToConcat.push(this.keyItems)
      }
      return [].concat(...arraysToConcat)
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
          this.dreamers = resp.dreamers;
          this.keyItems = resp.key_items;
          this.spoilerRetrieved = true
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    rowSelect(idx) {
      const index = this.selectedRows.indexOf(idx);
      if (index > -1) {
        this.selectedRows.splice(index, 1);
      } else {
        this.selectedRows.push(idx);
      }
    }
  },


};
</script>

<style>
.selected-row {
  background-color: #444444;
  color: #999999;
}

.selected-row:hover {
  background-color: #404040 !important;
  color: #999999;
}

th.text-start {
  background-color: #9cccff !important;
}
.v-input--selection-controls {
    margin-top: 0 !important;
    padding-top: 0 !important;
}


</style>