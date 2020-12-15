<template>
  <div class="hkr-item-table">
    <table>
      <tr v-for="(itemList, loc, idx) in dataToShow" :key="`${loc}-${idx}`">
        <th :class="`loc-${loc}`">{{ prettifyLocationName(loc) }}</th>
        <td>
          <v-card :class="`d-flex flex-wrap item-wrapper loc-${loc}`" flat tile>
            <div v-for="(item, jdx) in itemList" :key="`${item}-${idx}-${jdx}`">
              <tracker-image
                :src="`assets/hollow_knight/${item}.png`"
                :alt="`${item}`"
                :width="40"
                :height="40"
              />
            </div>
          </v-card>
        </td>
      </tr>
    </table>
  </div>
  <!-- <div class="hkr-item-table container">
    <v-card
      v-for="(itemList, loc, idx) in dataToShow"
      :key="`${loc}-${idx}`"
      :class="`d-flex flex-wrap loc-${loc} loc-card`"
      flat
      tile
    >
      <v-card-subtitle class="justify-center">{{ prettifyLocationName(loc) }}</v-card-subtitle>
      <v-card-text>
        <v-flex class="d-flex flex-wrap">
          <div v-for="(item, jdx) in itemList" :key="`${item}-${idx}-${jdx}`">
            <tracker-image
              :src="`assets/hollow_knight/${item}.png`"
              :alt="`${item}`"
              :width="40"
              :height="40"
            />
          </div>
        </v-flex>
      </v-card-text>
    </v-card>
  </div>-->
</template>

<script>
import TrackerImage from "@/components/HollowKnight/TrackerImage.vue";

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

export default {
  name: "HKRItemTable",
  data() {
    return {
      longLocNames,
    };
  },
  props: {
    dataToShow: Object,
  },
  computed: {
    locationsToShow() {
      return Object.keys(this.dataToShow);
    },
  },
  components: { TrackerImage },
  methods: {
    prettifyLocationName(loc) {
      const prettyLoc = prettifyLocationMapping[loc];
      return this.truncateLongLocNames(prettyLoc);
    },
    truncateLongLocNames(loc) {
      const a = this.longLocNames[loc] || loc;
      console.log(a);
      return a;
    },
  },
};
</script>

<style lang="scss" scoped>
$card-colors: (
  "Abyss": #bbbbbb,
  "Ancient_Basin": #979797,
  "City_of_Tears": #97a1c9,
  "Crystal_Peak": #e0b4e6,
  "Deepnest": #a6b7d0,
  "Dirtmouth": #a6a5a6,
  "Fog_Canyon": #c7a1c0,
  "Forgotten_Crossroads": #85afce,
  "Fungal_Wastes": #cbd1a6,
  "Greenpath": #9ac48f,
  "Hive": #beb077,
  "Howling_Cliffs": #999899,
  "Kingdoms_Edge": #ccbfac,
  "Queens_Gardens": #94b798,
  "Resting_Grounds": #b89378,
  "Royal_Waterways": #7fcecf,
);

@each $loc, $color in $card-colors {
  .loc-#{$loc} {
    background-color: $color !important;
  }
}

.container {
  display: grid;
  grid-template-columns: repeat(3, 110px);
  grid-template-rows: auto;
}

th {
  width: 3.2rem !important;
  font-family: "Open Sans Condensed", sans-serif;
  font-size: 2rem;
  font-weight: 600;
}

td {
  max-width: 170px;
  background-color: rgb(187, 185, 185) !important;
}

.item-wrapper {
  background-color: transparent;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 2px;
}
</style>