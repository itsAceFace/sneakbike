<template>
  <div class="hkr-item-table">
    <table>
      <tr v-for="(itemList, loc, idx) in locationOfItems" :key="`${loc}-${idx}`">
        <th v-if="locationsToShow.includes(loc)">{{ loc }}</th>
        <td v-if="locationsToShow.includes(loc)">
          <v-card class="d-flex flex-wrap item-wrapper" flat tile>
            <div v-for="(item, jdx) in itemList" :key="`${item}-${idx}-${jdx}`">
              <tracker-image
                v-if="itemsToShow.includes(mapItemToBaseItem(parseImageName(item)))"
                :src="`assets/hollow_knight/${mapItemToBaseItem(parseImageName(item))}.png`"
                :alt="`${mapItemToBaseItem(parseImageName(item))}`"
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

// Add dreamer nail stuff.
// TODO: WE CANT HAVE TWO OF THESE IN THIS AND HKRDREAMERCATCHER
// DRY THIS.
const itemToImageMapping = {
  Mothwing_Cloak: "Shade_Cloak",
  Shade_Soul: "Vengeful_Spirit",
  Descending_Dark: "Desolate_Dive",
  Abyss_Shriek: "Howling_Wraiths",
  Awoken_Dream_Nail: "Dream_Nail",
  Dream_Gate: "Dream_Gate",
};

export default {
  name: "HKRItemTable",
  data() {
    return {
      itemToImageMapping,
    };
  },
  props: {
    locationOfItems: Object,
    itemsToShow: Array,
    locationsToShow: Array,
  },
  components: { TrackerImage },
  methods: {
    mapItemToBaseItem(itemName) {
      if (Object.keys(itemToImageMapping).includes(itemName)) {
        return itemToImageMapping[itemName];
      } else {
        return itemName;
      }
    },
    parseImageName(itemName) {
      itemName = itemName.replace(/['\\]/g, "");
      itemName = itemName.replace(/ /g, "_");
      itemName = itemName.replace(/-.*/g, "");
      return itemName;
    },
  },
};
</script>

<style>
</style>