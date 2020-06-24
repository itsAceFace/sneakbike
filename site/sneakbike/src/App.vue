<template>
  <v-app id="inspire" light>
    <v-app-bar app color="indigo" clipped-left light>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>
        <span class="eight-bit-text toolbar-title">Sneakbike Mystery Race</span>
      </v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app clipped>
      <!-- TODO: Do a for loop here -->
      <v-list dense>
        <div v-for="(sidebarItem, index) in sidebarItems" :key="`sidebar-item-${index}`">
          <router-link :to="`${sidebarItem.link}`" tag="span">
            <v-list-item link>
              <v-list-item-action>
                <v-icon>{{sidebarItem.icon}}</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>{{sidebarItem.title}}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </router-link>
        </div>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col class="text-left">
            <div id="app">
              <router-view />
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
    <v-footer color="indigo" app>
      <span class="white--text">&copy; Team Sneakbike 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
const sidebarItems = [
  { icon: "mdi-view-dashboard", title: "Home", link: "/" },
  { icon: "mdi-cog", title: "Runner Setup", link: "/runner-setup" },
  { icon: "mdi-cog", title: "Runner Resources", link: "/runner-resources" },
  { icon: "mdi-cog", title: "Ranking Quiz!", link: "/ranking-quiz" },
  { icon: "mdi-cog", title: "Devops", link: "/devops" },
  { icon: "mdi-cog", title: "Cost Overhead", link: "/cost-overhead" }
];

export default {
  name: "App",
  data() {
    return {
      drawer: true,
      sidebarItems
    };
  }
};
</script>

<style lang="scss">
.eight-bit-text {
  font-family: "Press Start 2P", cursive;
}

.toolbar-title {
  font-size: 2rem;
}
</style>
