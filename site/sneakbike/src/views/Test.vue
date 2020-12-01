<template>
  <div>
    <v-row>
      <v-col cols="12" sm="8" offset-sm="2">
        <v-file-input
          truncate-length="120"
          accept=".txt"
          label="File input"
          @change="onFileChange"
        />
        <v-btn v-if="spoiler" @click="parseWithAPI">Submit</v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Test",
  data: function() {
    return {
      spoiler: "",
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
        this.spoiler = e.target.result;
      };
    },
    parseWithAPI() {
      axios
        .post("http://sb-api:8000/hkr/uploadspoiler/", {
          files: this.spoiler,
        })
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    },
  },
};
</script>
