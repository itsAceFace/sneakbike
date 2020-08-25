<template>
  <v-app id="inspire" light>
    <v-app-bar app color="indigo" clipped-left dense light>
      <v-app-bar-nav-icon large color="white" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>
        <span class="toolbar-title">Sneakbike</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn icon href="https://twitch.tv/sneakbike" target="_blank">
        <v-icon large color="white">mdi-twitch</v-icon>
      </v-btn>

      <v-btn icon href="https://www.github.com/jsal13/sneakbike/" target="_blank">
        <v-icon large color="white">mdi-github</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app clipped>
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
      <v-container>
        <v-row class="mb-6">
          <v-col sm="8" offset-sm="2">
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
  { icon: "mdi-anchor", title: "Home", link: "/" },
  { icon: "mdi-walk", title: "Runner Setup", link: "/runner-setup" },
  { icon: "mdi-pickaxe", title: "Runner Resources", link: "/runner-resources" },
  // { icon: "mdi-poll", title: "Ranking Quiz!", link: "/ranking-quiz" },
  { icon: "mdi-cloud", title: "Devops", link: "/devops" },
  // { icon: "mdi-brush", title: "Design Guide", link: "/design" },
  {
    icon: "mdi-radio-tower",
    title: "Hosting Sneakbike",
    link: "/hosting-sneakbike",
  },
  {
    icon: "mdi-currency-usd",
    title: "Cost Overhead",
    link: "/cost-overhead",
  },
];

export default {
  name: "App",
  data() {
    return {
      drawer: true,
      sidebarItems,
    };
  },
};
</script>

<style lang="scss">
.v-application {
  font-size: 16px !important;
  font-family: "Press Start 2P", cursive !important;
  line-height: 1.5 !important;
}

.toolbar-title {
  font-size: 1.5rem;
  font-family: "Press Start 2P", cursive;
  color: white;
}

p,
li,
th,
td,
.v-card__title,
.v-card__subtitle,
.v-list-item__title,
.v-radio > .v-label {
  font-family: "Roboto", sans-serif !important;
}

.v-card__text {
  padding-bottom: 0px !important;
}

ol,
ul {
  padding-bottom: 1rem;
}
li {
  padding-bottom: 0.35rem;
}

h1 {
  font-size: 1.25rem;
  padding-top: 1.25rem;
  padding-bottom: 1rem;
}

h2 {
  font-size: 1rem;
  padding-top: 1.25rem;
  padding-bottom: 1rem;
}

h3 {
  font-size: 0.75rem;
  padding-top: 1.25rem;
  padding-bottom: 1rem;
}
</style>
