<template>
  <div class="game-readme-gen-inputs">
    <v-container>
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
                    <div
                      class="overline mb-4"
                      style="max-width: 300px;"
                    >Game {{ gameidx + 1 }}: {{ $data[gameval]["title"] }}</div>
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
                    dense
                    @input="(v) => $set($data[gameval], key, v)"
                  />
                </div>
              </v-card>
            </div>
          </v-row>
        </v-col>
      </v-row>

      <v-row justify="center">
        <v-col cols="4" />
        <v-col cols="4">
          <v-btn @click="generate">Generate HTML</v-btn>
        </v-col>
        <v-col cols="4" />
      </v-row>
      <v-row justify="center">
        <v-col>
          <Prism v-if="html != ''" language="html">{{ html }}</Prism>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Prism from "vue-prism-component";

import gameReadmeRender from "@/utils/gameReadmeRender.js";

export default {
  name: "GameReadmeGenInputs",
  data() {
    return {
      game1: {
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
      },
      game2: {
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
      },
      game3: {
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
      },
      html: "",
    };
  },
  methods: {
    generate() {
      let gameArray = [this.game1, this.game2, this.game3];
      this.html = gameReadmeRender(gameArray);
    },
  },
  components: { Prism },
};
</script>
