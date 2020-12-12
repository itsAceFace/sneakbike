<template>
  <div class="hkr-item-table">
    <table>
      <tr v-for="(itemList, loc, idx) in dataToShow" :key="`${loc}-${idx}`">
        <th>{{ prettifyLocationName(loc) }}</th>
        <td>
          <v-card class="d-flex flex-wrap item-wrapper" flat tile>
            <div v-for="(item, jdx) in itemList" :key="`${item}-${idx}-${jdx}`">
              <tracker-image
                :src="`assets/hollow_knight/${item}.png`"
                :alt="`${item}`"
                :width="48"
                :height="48"
              />
            </div>
          </v-card>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import TrackerImage from "@/components/TrackerImage.vue";

const prettifyLocationMapping = {
  Royal_Waterways: "Royal Waterways",
  Howling_Cliffs: "Howling Cliffs",
  Dirtmouth: "Dirtmouth",
  Resting_Grounds: "Resting Grounds",
  Kingdoms_Edge: "Kingdoms Edge",
  City_of_Tears: "City of Tears",
  Greenpath: "Greenpath",
  Deepnest: "Deepnest",
  Forgotten_Crossroads: "Forgotten Crossroads",
  Fog_Canyon: "Fog Canyon",
  Fungal_Wastes: "Fungal Wastes",
  Ancient_Basin: "Ancient Basin",
  Crystal_Peak: "Crystal Peak",
  Queens_Gardens: "Queen's Gardens",
};

export default {
  name: "HKRItemTable",
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
      return prettifyLocationMapping[loc];
    },
  },
};
</script>

<style>
</style>