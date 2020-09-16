<template>
  <div class="toolbar-icons">
    <v-btn icon href="https://twitch.tv/sneakbike" target="_blank">
      <v-icon large color="black">mdi-twitch</v-icon>
    </v-btn>

    <v-btn icon href="https://www.youtube.com/channel/UC5WLNGgGQH2tpNHM5uk2kCg" target="_blank">
      <v-icon large color="black">mdi-youtube</v-icon>
    </v-btn>

    <v-btn icon href="https://www.github.com/jsal13/sneakbike/" target="_blank">
      <v-icon large color="black">mdi-github</v-icon>
    </v-btn>
  </div>
</template>

<script>
export default {
  name: "ToolbarIcons",
};
</script>

<style lang="scss" scoped>
.toolbar-icons {
  display: flex;
}
</style>