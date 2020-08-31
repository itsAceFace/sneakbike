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
            <v-row>
              <v-col v-for="(item, index) in runners" :key="`portrait-${index}`">
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

const teamMembers = [
  {
    imgSrc: "melat0nin.png",
    name: "melat0nin",
    twitchUsername: "melat0nin",
    jobs: "cofounder, ops, site maintainer, commentary",
    descriptionText: '"I think any% is making me into a monster."',
  },
  {
    imgSrc: "cosmicordia.png",
    name: "cosmicordia",
    twitchUsername: "cosmicordia",
    jobs: "cofounder, commentary",
    descriptionText: '"It\'s in the cultural zeitgeist."',
  },
  {
    imgSrc: "KiA00me.jpg",
    name: "KiA00me",
    twitchUsername: "KiA00me",
    jobs: "commentary",
    descriptionText: null,
  },
  {
    imgSrc: "placeholder.png",
    name: "Jen_theHuman",
    twitchUsername: "Jen_theHuman",
    jobs: "social media",
    descriptionText: null,
  },
];

const runners = [
  {
    name: "DangerDarin",
    imgSrc: "dangerdarin.png",
    twitchUsername: "dangerdarin",
    level: "beginner",
    descriptionText: null,
  },
  {
    name: "FlyingOctopus22",
    imgSrc: "placeholder.png",
    twitchUsername: "FlyingOctopus22",
    level: "advanced",
    descriptionText: null,
  },
  {
    name: "GhostMFLion",
    imgSrc: "placeholder.png",
    twitchUsername: "GhostMFLion",
    level: "advanced",
    descriptionText: null,
  },
  {
    name: "KiA00Me",
    imgSrc: "placeholder.png",
    twitchUsername: "KiA00Me",
    level: "advanced",
    descriptionText: null,
  },
  {
    name: "Jen_theHuman",
    imgSrc: "placeholder.png",
    twitchUsername: "Jen_theHuman",
    level: "beginner",
    descriptionText: null,
  },
  {
    name: "Rascalnicough",
    imgSrc: "placeholder.png",
    twitchUsername: "Rascalnicough",
    level: "advanced",
    descriptionText: null,
  },
  {
    name: "R11m1",
    imgSrc: "placeholder.png",
    twitchUsername: "R11m1",
    level: "beginner",
    descriptionText: null,
  },
  {
    name: "Super_Facts",
    imgSrc: "placeholder.png",
    twitchUsername: "Super_Facts",
    level: "advanced",
    descriptionText: null,
  },
  {
    name: "xchillhatterx",
    imgSrc: "placeholder.png",
    twitchUsername: "xchillhatterx",
    level: "beginner",
    descriptionText: null,
  },
];

export default {
  name: "Team",
  data() {
    return {
      teamMembers,
      runners,
    };
  },
  components: { TeamPortrait },
};
</script>
