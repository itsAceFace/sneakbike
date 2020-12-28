<template>
  <div class="runner-setup">
    <v-row justify="center">
      <v-col cols="12">
        <v-tabs v-model="tab" background-color="#92de69" centered icons-and-text>
          <v-tabs-slider></v-tabs-slider>

          <v-tab href="#runners">
            Runners
            <v-icon>mdi-controller-classic</v-icon>
          </v-tab>

          <v-tab href="#hosts">
            Hosts
            <v-icon>mdi-radio-tower</v-icon>
          </v-tab>

          <v-tab href="#developers">
            Developers
            <v-icon>mdi-code-greater-than</v-icon>
          </v-tab>
        </v-tabs>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col cols="1" />
      <v-col cols="10">
        <v-tabs-items :value="tab">
          <v-tab-item :value="'runners'">
            <SetupRunnerText />
          </v-tab-item>
          <v-tab-item :value="'hosts'">
            <SetupHostText />
          </v-tab-item>
          <v-tab-item :value="'developers'">
            <SetupDevText />
          </v-tab-item>
        </v-tabs-items>
      </v-col>
      <v-col cols="1" />
    </v-row>
  </div>
</template>

<script>
import SetupDevText from "@/components/Setup/DevText.vue";
import SetupRunnerText from "@/components/Setup/RunnerText.vue";
import SetupHostText from "@/components/Setup/HostText.vue";

export default {
  name: "Setup",
  computed: {
    tab: {
      set(tab) {
        this.$router.replace({ query: { ...this.$route.query, tab } });
      },
      get() {
        return this.$route.query.tab;
      },
    },
  },
  components: { SetupDevText, SetupRunnerText, SetupHostText },
};
</script>

