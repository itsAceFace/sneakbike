<template>
  <div>
    <div class="loc-div" :style="styleLocDiv">
      <div class="loc-circle" :style="styleLocCircle" @click="hideItems = !hideItems">
        <div class="loc-title-div">
          <span class="loc-title-text">{{ locAbbr }}</span>
        </div>
      </div>
      <div class="item-div" v-if="!hideItems">
        <v-flex class="d-flex flex-wrap">
          <div v-for="(item, jdx) in itemList" :key="`${item}-${jdx}`">
            <tracker-image
              :src="`assets/hollow_knight/${item}.png`"
              :alt="`${item}`"
              :width="40"
              :height="40"
              class="tracker-image"
            />
          </div>
        </v-flex>
      </div>
    </div>
  </div>
</template>
<script>
import TrackerImage from "@/components/HollowKnight/TrackerImage.vue";

export default {
  name: "HKRItemRect",
  data() {
    return {
      hideItems: false,
    };
  },
  components: { TrackerImage },
  props: {
    locAbbr: String,
    itemList: Array,
    colors: Object,
    zindex: Number,
  },
  computed: {
    styleLocDiv() {
      return `background-color: ${
        this.hideItems ? "transparent" : this.colors.background
      }; 
      border: 6px solid ${this.hideItems ? "transparent" : this.colors.border};
      width: ${70 + this.itemList.length * 41}px;`;
    },
    styleLocCircle() {
      return `background-color: ${this.colors.border};
      border: 2px solid ${this.colors.border};`;
    },
  },
};
</script>

<style lang="scss" scoped>
$height: 62px;
$large-radius: 4rem;
$item-starting-offset-left: 54px;
$item-starting-offset-top: 3px;

.loc-div {
  position: relative;
  height: $height;
  border-radius: $large-radius;
}
.loc-circle {
  position: absolute;
  width: $height - 6px;
  height: $height - 0px;
  top: -6px;
  left: -6px;
  border-top-left-radius: $large-radius;
  border-bottom-left-radius: $large-radius;
  padding: 0;
  margin: 0;
}

.loc-title-div {
  position: absolute;
  left: 15px;
  top: 13px;
}
.loc-title-text {
  font-family: "Roboto", sans-serif;
  font-size: 1rem;
  font-weight: 500;
  color: white;
  -webkit-user-select: none; /* Safari */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* IE10+/Edge */
  user-select: none; /* Standard */
  cursor: default;
}

.item-div {
  position: absolute;
  left: $item-starting-offset-left;
  top: $item-starting-offset-top;
}
</style>