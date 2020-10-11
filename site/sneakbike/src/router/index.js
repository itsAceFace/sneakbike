import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Schedule from "@/views/Schedule.vue";
import Quiz from "@/views/Quiz.vue";

import ResolutionStandards from "@/views/ResolutionStandards.vue";
import Team from "@/views/Team.vue";
import ScoreBoard from "@/views/ScoreBoard.vue";
import GameReadmeGen from "@/views/GameReadmeGen.vue";
import RacedayChecklist from "@/views/RacedayChecklist.vue";
import NightbotCommands from "@/views/NightbotCommands.vue";

import Setup from "@/views/Setup.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/schedule",
    name: "Schedule",
    component: Schedule,
  },
  {
    path: "/setup",
    name: "Setup",
    component: Setup,
  },

  {
    path: "/resolution-standards",
    name: "ResolutionStandards",
    component: ResolutionStandards,
  },
  {
    path: "/team",
    name: "Team",
    component: Team,
  },
  {
    path: "/scoreboard",
    name: "ScoreBoard",
    component: ScoreBoard,
  },
  {
    path: "/quiz",
    name: "Quiz",
    component: Quiz,
  },
  { path: "/readme", name: "GameReadmeGen", component: GameReadmeGen },
  { path: "/checklist", name: "RacedayChecklist", component: RacedayChecklist },
  { path: "/nightbot", name: "NightbotCommands", component: NightbotCommands },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
