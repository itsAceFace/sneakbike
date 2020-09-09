import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import SneakbikeInfo from "@/views/SneakbikeInfo.vue";
import Quiz from "@/views/Quiz.vue";
import EmulatorSetup from "@/views/EmulatorSetup.vue";
import ResolutionStandards from "@/views/ResolutionStandards.vue";
import Team from "@/views/Team.vue";
import ScoreBoard from "@/views/ScoreBoard.vue";
import GameReadmeGen from "@/views/GameReadmeGen.vue";

import RunnerSetup from "@/views/RunnerSetup.vue";
import HostSetup from "@/views/HostSetup.vue";
import DevSetup from "@/views/DevSetup.vue";

import RunnerTroubleshooting from "@/views/RunnerTroubleshooting.vue";
import HostTroubleshooting from "@/views/HostTroubleshooting.vue";
import DevTroubleshooting from "@/views/DevTroubleshooting.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/sneakbike-info",
    name: "SneakbikeInfo",
    component: SneakbikeInfo,
  },
  {
    path: "/runner-setup",
    name: "RunnerSetup",
    component: RunnerSetup,
  },
  {
    path: "/runner-troubleshooting",
    name: "RunnerTroubleshooting",
    component: RunnerTroubleshooting,
  },
  {
    path: "/host-setup",
    name: "HostSetup",
    component: HostSetup,
  },
  {
    path: "/host-troubleshooting",
    name: "HostTroubleshooting",
    component: HostTroubleshooting,
  },
  {
    path: "/dev-setup",
    name: "DevSetup",
    component: DevSetup,
  },
  {
    path: "/dev-troubleshooting",
    name: "DevTroubleshooting",
    component: DevTroubleshooting,
  },
  {
    path: "/emulator-setup",
    name: "EmulatorSetup",
    component: EmulatorSetup,
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
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
