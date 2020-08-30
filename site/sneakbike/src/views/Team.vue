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
            <v-row>
              <v-col v-for="(item, index) in teamMembers" :key="`portrait-${index}`">
                <TeamPortrait
                  :name="item.name"
                  :imgSrc="item.imgSrc"
                  :jobs="item.jobs"
                  :twitchUsername="item.twitchUsername"
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

const teamMembers = [
  {
    imgSrc: "melat0nin.png",
    name: "melat0nin",
    twitchUsername: "melat0nin",
    jobs: "cofounder, site maintainer, ops, commentary",
  },
  {
    imgSrc: "cosmicordia.png",
    name: "cosmicordia",
    twitchUsername: "cosmicordia",
    jobs: "cofounder, commentary",
  },
  {
    imgSrc: "kia00me.png",
    name: "KiA00me",
    twitchUsername: "KiA00me",
    jobs: "commentary",
  },
  {
    imgSrc: "jen_thehuman.png",
    name: "Jen_theHuman",
    twitchUsername: "Jen_theHuman",
    jobs: "social media",
  },
];

export default {
  name: "Team",
  data() {
    return {
      teamMembers,
    };
  },
  components: { TeamPortrait },
};
</script>
