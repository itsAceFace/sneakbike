<template>
  <v-expansion-panel>
    <v-expansion-panel-header>Options</v-expansion-panel-header>
    <v-expansion-panel-content>
      <v-switch
        :label="'Blue Screen Mode (For OBS Displaying)?'"
        @change="toggleBlueScreen"
        v-model="blueScreen"
      />
      <v-switch
        :label="'Show Dreamers?'"
        @change="toggleDreamersAndRefresh()"
        :input-value="showDreamers"
      />
      <v-switch
        :label="'Show Abilities?'"
        @change="toggleAbilitiesAndRefresh()"
        :input-value="showAbilities"
      />
      <v-switch
        :label="'Show Useful Items?'"
        @change="toggleUsefulItemsAndRefresh()"
        :input-value="showUsefulItems"
      />
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "HKRItemToggle",
  data() {
    return { blueScreen: false };
  },
  computed: {
    ...mapState("hkr", ["showDreamers", "showAbilities", "showUsefulItems"]),
  },
  methods: {
    ...mapActions("hkr", [
      "toggleDreamersAndRefresh",
      "toggleAbilitiesAndRefresh",
      "toggleUsefulItemsAndRefresh",
    ]),
    toggleBlueScreen() {
      document.getElementById("app").style.background = this.blueScreen
        ? "rgb(0,0,255)"
        : "";
    },
  },
  beforeDestroy() {
    document.getElementById("app").style.background = "";
  },
};
</script>