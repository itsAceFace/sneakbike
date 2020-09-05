<template>
  <div class="toolbar-dropdowns">
    <ToolbarDropdown :name="'Info'" :pageList="infoPages" />
    <ToolbarDropdown :name="'Runners'" :pageList="runnerPages" />
    <ToolbarDropdown :name="'Hosts'" :pageList="hostPages" />
    <ToolbarDropdown :name="'Developers'" :pageList="devPages" />
    <ToolbarDropdown :name="'Resources'" :pageList="resourcesPages" />
  </div>
</template>

<script>
import ToolbarDropdown from "@/components/ToolbarDropdown.vue";

const infoPages = [
  { name: "Sneakbike Info", route: "/sneakbike-info" },
  { name: "Team", route: "/team" },
  // { name: "Scoreboard", route: "/scoreboard" },
];

const runnerPages = [
  { name: "Setup For Runners", route: "/runner-setup" },
  // { name: "Runner Troubleshooting", route: "/runner-troubleshooting" },
  { name: "Emulator Setup", route: "/emulator-setup" },
];

const hostPages = [
  { name: "Setup For Hosts", route: "/host-setup" },
  // { name: "Host Troubleshooting", route: "/host-troubleshooting" },
];

const devPages = [
  { name: "Setup For Devs", route: "/dev-setup" },
  // { name: "Dev Troubleshooting", route: "/dev-troubleshooting" },
];

const resourcesPages = [
  { name: "Resolution Standards", route: "/resolution-standards" },
];

export default {
  name: "ToolbarDropdowns",
  data() {
    return {
      runnerPages,
      hostPages,
      devPages,
      infoPages,
      resourcesPages,
    };
  },
  components: { ToolbarDropdown },
};
</script>

<style lang="scss" scoped>
.toolbar-dropdowns {
  display: flex;
}
</style>