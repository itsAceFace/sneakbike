import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";

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
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
