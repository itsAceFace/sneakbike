<template>
  <div class="team">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <h1>Team Sneakbike!</h1>
        </v-col>
        <v-col cols="2" />
      </v-row>
    </v-container>

    <v-row>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-card>
          <v-container fluid>
            <v-row :align="'center'" :justify="'center'">
              <v-col
                v-for="(item, index) in team"
                :key="`portrait-${index}`"
                style="flex-grow: 0 !important"
              >
                <TeamPortrait
                  :name="item.name"
                  :imgSrc="item.imgSrc"
                  :hoverInfo="item.jobs"
                  :twitchUsername="item.twitchUsername"
                  :descriptionText="item.descriptionText"
                />
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>

    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <h1>Sneakbike Runners!</h1>
        </v-col>
        <v-col cols="2" />
      </v-row>
    </v-container>

    <v-row>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-card>
          <v-container fluid>
            <v-row :align="'center'" :justify="'center'">
              <v-col
                v-for="(item, index) in runners"
                :key="`portrait-${index}`"
                style="flex-grow: 0 !important"
              >
                <TeamPortrait
                  :name="item.name"
                  :imgSrc="item.imgSrc"
                  :hoverInfo="item.level"
                  :twitchUsername="item.twitchUsername"
                  :descriptionText="item.descriptionText"
                />
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import TeamPortrait from "@/components/TeamPortrait.vue";
import team from "@/data/team.js";
import runners from "@/data/runners.js";

export default {
  name: "Team",
  data() {
    return {
      team,
      runners,
    };
  },
  components: { TeamPortrait },
};
</script>
