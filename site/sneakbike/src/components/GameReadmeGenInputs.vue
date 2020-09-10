<template>
  <div class="game-readme-gen-inputs">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <v-row justify="center" align="center">
            <v-btn @click="downloadHTML">Download HTML</v-btn>
          </v-row>
        </v-col>
        <v-col cols="2" />
      </v-row>
      <br />
      <v-row justify="center">
        <v-col cols>
          <v-row align="center" justify="center">
            <div
              v-for="(gameval, gameidx) in ['game1', 'game2', 'game3']"
              :key="`game-${gameidx + 1}`"
              style="padding-left: 1rem; padding-right: 1rem;"
            >
              <v-card class="mx-auto" max-width="312" shaped color="#fefefe">
                <v-list-item>
                  <v-list-item-content>
                    <div class="overline mb-4" style="max-width: 300px;">
                      Game {{ gameidx + 1 }}: {{ $data[gameval]["title"] }}
                    </div>
                  </v-list-item-content>
                </v-list-item>

                <div
                  v-for="(value, key, index) in $data[gameval]"
                  :key="`item-${gameidx + 1}-${index}`"
                  style="padding-left: 4px; padding-right: 4px;"
                >
                  <v-textarea
                    outlined
                    :label="key.toUpperCase()"
                    placeholder=" "
                    :height="
                      ['title', 'objective', 'hints'].includes(key) ? 64 : 48
                    "
                    no-resize
                    dense
                    @input="(v) => $set($data[gameval], key, v)"
                  />
                </div>
              </v-card>
            </div>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { saveAs } from "file-saver";
import gameReadmeRender from "@/utils/gameReadmeRender.js";

const gameItems = {
  title: "",
  objective: "",
  hints: "",
  a: "",
  b: "",
  x: "",
  y: "",
  l: "",
  r: "",
  start: "",
  select: "",
  up: "",
  down: "",
  left: "",
  right: "",
};

export default {
  name: "GameReadmeGenInputs",
  data() {
    return {
      game1: this._.clone(gameItems),
      game2: this._.clone(gameItems),
      game3: this._.clone(gameItems),
      html: "",
    };
  },
  methods: {
    downloadHTML() {
      let gameArray = [this.game1, this.game2, this.game3];
      this.html = gameReadmeRender(gameArray);

      let file = new File([this.html], "README_Sneakbike.html", {
        type: "text/plain;charset=utf-8",
      });
      saveAs(file);
    },
  },
};
</script>
