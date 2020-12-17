<template>
  <div class="hkr-item-table">
    <div style="margin-top: 1.0rem; margin-bottom: 1.0rem;">
      <v-flex class="d-flex flex-wrap">
        <div v-for="(itemList, loc, idx) in dataToShow" :key="`chip-${loc}-${idx}`">
          <v-chip
            class="ma-1"
            :class="{'dimmed-chip': !locData[loc]['show']}"
            :color="locData[loc]['background']"
            @click="toggleRectangle(loc)"
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

// 303030 and 000001 are placeholders.
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
    abbr: "Basin",
    show: true,
  },
  City_of_Tears: {
    background: "#6b89a9",
    border: "#1b4a7b",
    abbr: "CoT",
    show: true,
  },
  Crystal_Peak: {
    background: "#303030",
    border: "#000001",
    abbr: "Cry",
    show: true,
  },
  Deepnest: {
    background: "#666b80",
    border: "#141c3c",
    abbr: "Deep",
    show: true,
  },
  Dirtmouth: {
    background: "#787994",
    border: "#2f315b",
    abbr: "Dirt",
    show: true,
  },
  Fog_Canyon: {
    background: "#303030",
    border: "#000001",
    abbr: "Fog",
    show: true,
  },
  Forgotten_Crossroads: {
    background: "#687796",
    border: "#202d5d",
    abbr: "xRoad",
    show: true,
  },
  Fungal_Wastes: {
    background: "#303030",
    border: "#000001",
    abbr: "Fung",
    show: true,
  },
  Greenpath: {
    background: "#679487",
    border: "#155b47",
    abbr: "GPath",
    show: true,
  },
  Hive: { background: "#303030", border: "#000001", abbr: "Hive", show: true },
  Howling_Cliffs: {
    background: "#303030",
    border: "#000001",
    abbr: "Howl",
    show: true,
  },
  Kingdoms_Edge: {
    background: "#303030",
    border: "#000001",
    abbr: "KEdge",
    show: true,
  },
  Queens_Gardens: {
    background: "#303030",
    border: "#000001",
    abbr: "QuGa",
    show: true,
  },
  Resting_Grounds: {
    background: "#84799d",
    border: "#423169",
    abbr: "Rest",
    show: true,
  },
  Royal_Waterways: {
    background: "#6d919d",
    border: "#1e5669",
    abbr: "Water",
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
    toggleRectangle(loc) {
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