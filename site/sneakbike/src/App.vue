<template>
  <v-app>
    <div id="nav">
      <v-app-bar app flat color="#92de69">
        <v-toolbar-title>Sneakbike</v-toolbar-title>
        <ToolbarDropdowns />
        <v-spacer />
        <ToolbarIcons />
      </v-app-bar>
    </div>

    <v-main>
      <!-- <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>-->
      <!-- </div> -->
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import ToolbarDropdowns from "@/components/ToolbarDropdowns.vue";
import ToolbarIcons from "@/components/ToolbarIcons.vue";

export default {
  name: "App",
  components: { ToolbarDropdowns, ToolbarIcons },
};
</script>

<style lang="scss">
$base-font-size: 20px;
$base-heading-top-padding: 2rem;
$base-heading-bottom-padding: 0.75rem;

#app {
  font-family: "Roboto", sans-serif;
  font-size: $base-font-size;
}

.v-toolbar__title {
  font-family: "Press Start 2P", cursive;
  font-size: 1.5rem !important;
  padding-right: 1.5rem;
}

h1,
h2,
h3,
h4 {
  font-family: "Press Start 2P", cursive;
  padding-top: $base-heading-top-padding;
}

h1 {
  font-size: 2rem;
  padding-bottom: $base-heading-bottom-padding;
}

h2 {
  font-size: 1.5rem;
  padding-bottom: $base-heading-bottom-padding;
}

h3 {
  font-size: 1.25rem;
}
</style>
