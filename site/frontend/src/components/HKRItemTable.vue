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
                :width="40"
                :height="40"
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
  Howling_Cliffs: "Howling Cliffs",
  Kingdoms_Edge: "Kingdoms Edge",
  Queens_Gardens: "Queen's Gardens",
  Resting_Grounds: "Resting Grounds",
  Royal_Waterways: "Royal Waterways",
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
th {
  font-size: 1rem;
  max-width: 150px;
  padding: 2px;
}
td {
  max-width: 250px;
}
</style>