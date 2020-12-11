<template>
  <div class="tracker-image">
    <img
      :src="require(`@/${src}`)"
      :class="{ 'item-found': itemFound }"
      @click="itemFound = !itemFound"
      :width="width"
      :height="height"
      :alt="`${alt}`"
      :title="`${alt}`"
    />
  </div>
</template>

<script>
export default {
  name: "TrackerImage",
  props: {
    src: String,
    alt: String,
    width: Number,
    height: Number,
  },
  data() {
    return { itemFound: false };
  },
};
</script>

<style>
.item-found {
  opacity: 0.3;
}
img {
  padding-top: 0 !important;
  padding-bottom: 0 !important;
  padding-left: 2px !important;
  padding-right: 2px !important;
}
</style>