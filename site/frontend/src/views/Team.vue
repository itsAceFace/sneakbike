<template>
  <div class="team">
    <v-container>
      <v-row justify="center" align="center">
        <h1 class="team">Team Sneakbike!</h1>
      </v-row>
    </v-container>

    <v-row>
      <v-col cols="12" sm="8" offset-sm="2">
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
  </div>
</template>

<script>
import TeamPortrait from "@/components/TeamPortrait.vue";
import team from "@/data/team.js";

export default {
  name: "Team",
  data() {
    return {
      team
    };
  },
  components: { TeamPortrait },
};
</script>

<style lang="scss" scoped>
h1.team {
  font-family: "Press Start 2P", cursive !important;
}
</style>