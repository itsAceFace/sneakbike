<template>
  <div class="hkr-item-table">
    <div style="margin-top: 1.0rem; margin-bottom: 1.0rem;">
      <v-flex class="d-flex flex-wrap">
        <div v-for="(itemList, loc, idx) in dataToShow" :key="`chip-${loc}-${idx}`">
          <v-chip
            class="ma-1"
            :class="{'dimmed-chip': !locData[loc]['show']}"
            :color="locData[loc]['background']"
            @click="toggleLoc(loc)"
          >
            <span class="chip-text">{{ prettifyLocNames(loc) }}</span>
          </v-chip>
        </div>
      </v-flex>
    </div>
    <hr />

    <div style="margin-top: 1.0rem;">
      <div v-for="(itemList, loc, idx) in dataToShow" :key="`rect-${loc}-${idx}`">
        <HKRItemRect
          v-if="locData[loc]['show']"
          @circleClicked="toggleLoc(loc, item)"
          :locData="locData[loc]"
          :itemList="itemList"
          :zindex="idx + 10"
          class="hkr-item-rectangle"
        />
      </div>
    </div>
  </div>
</template>

<script>
import HKRItemRect from "@/components/HollowKnight/HKRItemRect.vue";

// 303030 and000001 are placeholders.

const locData = {
  Abyss: {
    background: "#707170",
    border: "#242524",
    abbr: "Abyss",
    show: true,
  },
  Ancient_Basin: {
    background: "#73747d",
    border: "#282a37",
    abbr: "AnBsn",
    show: true,
  },
  City_of_Tears: {
    background: "#6b89a9",
    border: "#1b4a7b",
    abbr: "CityT",
    show: true,
  },
  Crystal_Peak: {
    background: "#b588b0",
    border: "#95568f",
    abbr: "CryPk",
    show: true,
  },
  Deepnest: {
    background: "#666b80",
    border: "#141c3c",
    abbr: "DNest",
    show: true,
  },
  Dirtmouth: {
    background: "#787994",
    border: "#2f315b",
    abbr: "Dirtm",
    show: true,
  },
  Fog_Canyon: {
    background: "#9da3bd",
    border: "#5b6591",
    abbr: "FogCn",
    show: true,
  },
  Forgotten_Crossroads: {
    background: "#687796",
    border: "#202d5d",
    abbr: "FxRds",
    show: true,
  },
  Fungal_Wastes: {
    background: "#58747c",
    border: "#113945",
    abbr: "FungW",
    show: true,
  },
  Greenpath: {
    background: "#679487",
    border: "#155b47",
    abbr: "GPath",
    show: true,
  },
  Hive: { background: "#303030", border: "#000001", abbr: "", show: true },
  Howling_Cliffs: {
    background: "#75809a",
    border: "#3b4a6f",
    abbr: "HClif",
    show: true,
  },
  Kingdoms_Edge: {
    background: "#768384",
    border: "#3c4e50",
    abbr: "KEdge",
    show: true,
  },
  Queens_Gardens: {
    background: "#559f9d",
    border: "#0d7673",
    abbr: "QGdn",
    show: true,
  },
  Resting_Grounds: {
    background: "#84799d",
    border: "#423169",
    abbr: "RestG",
    show: true,
  },
  Royal_Waterways: {
    background: "#6d919d",
    border: "#1e5669",
    abbr: "RWatr",
    show: true,
  },
};

export default {
  name: "HKRItemTable",
  data() {
    return {
      locData,
    };
  },
  props: {
    dataToShow: Object,
  },
  components: { HKRItemRect },
  computed: {
    locationsToShow() {
      return Object.keys(this.dataToShow);
    },
  },
  methods: {
    truncateLongLocNames(loc) {
      const a = this.locData[loc]["abbr"] || loc;
      return a;
    },
    prettifyLocNames(loc) {
      const possessives = {
        Queens_Gardens: "Queen's Gardens",
        Kingdoms_Edge: "Kingdom's Edge",
      };
      if (Object.keys(possessives).includes(loc)) {
        return possessives[loc];
      } else {
        return loc.replaceAll("_", " ");
      }
    },
    toggleLoc(loc) {
      this.$set(this.locData[loc], "show", !this.locData[loc]["show"]);
    },
  },
};
</script>

<style scoped>
.hkr-item-rectangle {
  margin-top: -6px;
}
.chip-text {
  color: white;
  -webkit-user-select: none; /* Safari */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* IE10+/Edge */
  user-select: none; /* Standard */
  cursor: default;
}

.dimmed-chip {
  opacity: 0.5;
}
</style>