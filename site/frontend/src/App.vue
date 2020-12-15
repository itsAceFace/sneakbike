<template>
  <v-app>
    <div id="nav">
      <v-app-bar app flat color="#92de69">
        <v-app-bar-nav-icon @click="drawer = !drawer" />
        <v-toolbar-title>
          <router-link to="/">Sneakbike</router-link>
        </v-toolbar-title>
        <!-- <ToolbarDropdowns /> -->
        <v-spacer />
        <ToolbarIcons />
      </v-app-bar>
    </div>

    <div id="sidebar">
      <v-navigation-drawer v-model="drawer" app>
        <v-list>
          <SidebarList :name="'Home'" :pageList="homePages" />
          <SidebarList :name="'Info'" :pageList="infoPages" />
          <SidebarList :name="'Setup'" :pageList="setupPages" />
          <v-divider />

          <!-- Sneakbike-Ops Resources -->
          <div class="sidebar-list">
            <v-list-group no-action>
              <template v-slot:activator>
                <v-list-item-content>
                  <v-list-item-title>Ops Resources</v-list-item-title>
                </v-list-item-content>
              </template>

              <v-list-item
                v-for="(item, index) in resourcesPages"
                :key="`${item['name']}-${index}`"
                :to="item.route"
              >
                <v-list-item-content>
                  <v-list-item-title v-text="item.name" />
                </v-list-item-content>
              </v-list-item>
            </v-list-group>
          </div>

          <!-- HKR Resources -->
          <div class="sidebar-list">
            <v-list-group no-action>
              <template v-slot:activator>
                <v-list-item-content>
                  <v-list-item-title>Hollow Knight Rando</v-list-item-title>
                </v-list-item-content>
              </template>

              <v-list-item
                v-for="(item, index) in hollowKnightRandoPages"
                :key="`${item['name']}-${index}`"
                :to="item.route"
              >
                <v-list-item-content>
                  <v-list-item-title v-text="item.name" />
                </v-list-item-content>
              </v-list-item>
            </v-list-group>
          </div>
        </v-list>
      </v-navigation-drawer>
    </div>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
const homePages = [{ name: "Home", route: "/" }];
const infoPages = [
  { name: "Schedule", route: "/schedule" },
  { name: "Team", route: "/team" },
  // { name: "Scoreboard", route: "/scoreboard" },
];

const setupPages = [{ name: "Sneakbike Setup", route: "/setup" }];

const resourcesPages = [
  { name: "Resolution Standards", route: "/resolution-standards" },
  { name: "README Generator", route: "/readme" },
  { name: "Race Day Checklist", route: "/checklist" },
  { name: "Nightbot Command Updates", route: "/nightbot" },
];

const hollowKnightRandoPages = [
  { name: "QuickMode Spoiler Tool", route: "/hkr/dream-catcher" },
];

import ToolbarIcons from "@/components/BaseSection/ToolbarIcons.vue";
import SidebarList from "@/components/BaseSection/SidebarList.vue";

export default {
  name: "App",
  components: { ToolbarIcons, SidebarList },
  data() {
    return {
      drawer: false,
      homePages,
      infoPages,
      setupPages,
      resourcesPages,
      hollowKnightRandoPages,
    };
  },
};
</script>

<style lang="scss">
$base-font-size: 18px;
$base-heading-top-padding: 2rem;
$base-heading-bottom-padding: 0.75rem;

#app {
  font-family: "Lora", serif;
  font-size: $base-font-size;
}

// Sneakbike Title
.v-toolbar__title > a {
  font-family: "Press Start 2P", cursive;
  font-size: 1.5rem !important;
  color: black !important;
  text-decoration: none !important;
}

.v-list-item__content {
  font-family: "Lato", sans-serif;
  font-weight: bold;
}

h1,
h2,
h3,
h4 {
  font-family: "Lato", sans-serif;
}

h1 {
  font-variant: small-caps;
}

h1 {
  font-size: 2rem;
  padding-bottom: $base-heading-bottom-padding;
}

h2 {
  font-size: 1.5rem;
  padding-top: $base-heading-top-padding;
  padding-bottom: $base-heading-bottom-padding;
}

h3 {
  font-size: 1.25rem;
}

.warning-card,
.info-card {
  padding-top: 1rem;
  padding-bottom: 1rem;
}

a {
  text-decoration: none;
}

ul {
  margin-bottom: 1rem;
}

pre[class*="language-"] {
  font-size: 1rem !important;
  margin-top: 1.5rem !important;
  margin-bottom: 1.5rem !important;
}

img {
  max-width: 100%;
  padding-top: 1rem;
  padding-bottom: 1rem;
}

.v-application--is-ltr
  .v-list-group--no-action
  > .v-list-group__items
  > .v-list-item {
  padding-left: 24px;
}
</style>
