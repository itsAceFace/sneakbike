<template>
  <div class="tracker-image">
    <v-img
      :src="require(`@/${src}`)"
      :class="{ 'item-found': itemFound }"
      @click="itemFound = !itemFound"
      :height="height"
      :width="width"
      :alt="`${alt}`"
    />
  </div>
</template>

<script>
export default {
  name: "TrackerImage",
  props: {
    src: String,
    alt: String,
    height: Number,
    width: Number,
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
</style>