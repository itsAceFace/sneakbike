<template>
  <div class="hkr-item-table container">
    <v-card
      v-for="(itemList, loc, idx) in dataToShow"
      :key="`${loc}-${idx}`"
      :class="`d-flex flex-wrap item-wrapper ${loc}`"
      flat
    >
      <v-card-subtitle>{{ prettifyLocationName(loc) }}</v-card-subtitle>
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
  Hive: "Hive",
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

<style scoped>
.item-wrapper {
  margin-bottom: 0 !important;
  padding-left: 0.5rem !important;
  padding-right: 0.5rem !important;
  /* background: #5f5f5f !important; */
}

.container {
  display: grid;
  align-items: center;
  grid-template-rows: auto;
  grid-template-columns: 240px;
}

.v-card__subtitle,
.v-card__text {
  padding: 0 !important;
  color: white !important;
  font-family: Cambria, Cochin, Georgia, Times, "Times New Roman", serif !important;
}

/* TODO: Hm, I dunno how to do this better.  SCSS? */
.Abyss {
  background-color: #141614ee;
  border: 2px solid #737373;
  border-radius: 0.25rem;
}
.Ancient_Basin {
  background-color: #292929ee;
  border: 2px solid #b5b6b5;
  border-radius: 0.25rem;
}
.City_of_Tears {
  background-color: #242839ee;
  border: 2px solid #c8d3ff;
  border-radius: 0.25rem;
}
.Crystal_Peak {
  background-color: #342b35ee;
  border: 2px solid #e5beea;
  border-radius: 0.25rem;
}
.Deepnest {
  background-color: #21272cee;
  border: 2px solid #a6b7d0;
  border-radius: 0.25rem;
}
.Dirtmouth {
  background-color: #272827ee;
  border: 2px solid #a6a5a6;
  border-radius: 0.25rem;
}
.Fog_Canyon {
  background-color: #392e37ee;
  border: 2px solid #edc3e5;
  border-radius: 0.25rem;
}
.Forgotten_Crossroads {
  background-color: #273238ee;
  border: 2px solid #a9cfea;
  border-radius: 0.25rem;
}
.Fungal_Wastes {
  background-color: #383b2eee;
  border: 2px solid #e4eac0;
  border-radius: 0.25rem;
}
.Greenpath {
  background-color: #2d3b2aee;
  border: 2px solid #d4ffc9;
  border-radius: 0.25rem;
}
.Hive {
  background-color: #38351fee;
  border: 2px solid #e3d18b;
  border-radius: 0.25rem;
}
.Howling_Cliffs {
  background-color: #131413ee;
  border: 2px solid #777677;
  border-radius: 0.25rem;
}
.Kingdoms_Edge {
  background-color: #312d28ee;
  border: 2px solid #dfd1be;
  border-radius: 0.25rem;
}
.Queens_Gardens {
  background-color: #1e271eee;
  border: 2px solid #94b798;
  border-radius: 0.25rem;
}
.Resting_Grounds {
  background-color: #35291fee;
  border: 2px solid #e6b593;
  border-radius: 0.25rem;
}
.Royal_Waterways {
  background-color: #1f3b39ee;
  border: 2px solid #93f7f8;
  border-radius: 0.25rem;
}
</style>