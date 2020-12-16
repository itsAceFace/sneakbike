<template>
  <div style="margin-top: 1rem;">
    <div v-for="(itemList, loc, idx) in dataToShow" :key="`${loc}-${idx}`">
      <HKRItemRect
        :locAbbr="prettifyLocationName(loc)"
        :itemList="itemList"
        :colors="locColors[loc]"
        :zindex="idx + 10"
        class="hkr-item-rectangle"
      />
    </div>
  </div>
</template>

<script>
// import TrackerImage from "@/components/HollowKnight/TrackerImage.vue";
import HKRItemRect from "@/components/HollowKnight/HKRItemRect.vue";

const prettifyLocationMapping = {
  Abyss: "Abyss",
  Ancient_Basin: "Ancient Basin",
  City_of_Tears: "City of Tears",
  Crystal_Peak: "Crystal Peak",
  Deepnest: "Deepnest",
  Dirtmouth: "Dirtmouth",
  Fog_Canyon: "Fog Canyon",
  Forgotten_Crossroads: "Forgotten Crossroads",
  Fungal_Wastes: "Fungal Wastes",
  Greenpath: "Greenpath",
  Hive: "Hive",
  Howling_Cliffs: "Howling Cliffs",
  Kingdoms_Edge: "Kingdoms Edge",
  Queens_Gardens: "Queen's Gardens",
  Resting_Grounds: "Resting Grounds",
  Royal_Waterways: "Royal Waterways",
};

const longLocNames = {
  Abyss: "ABY",
  "Ancient Basin": "AB",
  "City of Tears": "CT",
  "Crystal Peak": "CP",
  Deepnest: "DN",
  Dirtmouth: "DM",
  "Fog Canyon": "FC",
  "Forgotten Crossroads": "FXR",
  "Fungal Wastes": "FW",
  Greenpath: "GP",
  Hive: "HV",
  "Howling Cliffs": "HC",
  "Kingdoms Edge": "KE",
  "Queen's Gardens": "QG",
  "Resting Grounds": "RG",
  "Royal Waterways": "RW",
};

const locColors = {
  Abyss: { background: "#707170", border: "#242524" },
  Ancient_Basin: { background: "#73747d", border: "#282a37" },
  City_of_Tears: { background: "#6b89a9", border: "#1b4a7b" },
  Crystal_Peak: { background: "#000001", border: "#000001" },
  Deepnest: { background: "#666b80", border: "#141c3c" },
  Dirtmouth: { background: "#787994", border: "#2f315b" },
  Fog_Canyon: { background: "#000000", border: "#000001" },
  Forgotten_Crossroads: { background: "#687796", border: "#202d5d" },
  Fungal_Wastes: { background: "#000001", border: "#000001" },
  Greenpath: { background: "#679487", border: "#155b47" },
  Hive: { background: "#000001", border: "#000001" },
  Howling_Cliffs: { background: "#000001", border: "#000001" },
  Kingdoms_Edge: { background: "#000001", border: "#000001" },
  Queens_Gardens: { background: "#000001", border: "#000001" },
  Resting_Grounds: { background: "#84799d", border: "#423169" },
  Royal_Waterways: { background: "#6d919d", border: "#1e5669" },
};

export default {
  name: "HKRItemTable",
  data() {
    return {
      longLocNames,
      locColors,
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
  // components: { TrackerImage },
  methods: {
    prettifyLocationName(loc) {
      const prettyLoc = prettifyLocationMapping[loc];
      return this.truncateLongLocNames(prettyLoc);
    },
    truncateLongLocNames(loc) {
      const a = this.longLocNames[loc] || loc;
      return a;
    },
  },
};
</script>

<style scoped>
.hkr-item-rectangle {
  margin-top: -7px;
}
</style>