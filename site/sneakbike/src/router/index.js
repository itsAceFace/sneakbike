import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Devops from "../views/Devops.vue";
import RunnerSetup from "../views/RunnerSetup.vue";
import RunnerResources from "../views/RunnerResources.vue";
import CostOverhead from "../views/CostOverhead.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/devops",
    name: "Devops",
    component: Devops
  },
  {
    path: "/runner-setup",
    name: "RunnerSetup",
    component: RunnerSetup
  },
  {
    path: "/runner-resources",
    name: "RunnerResources",
    component: RunnerResources
  },
  {
    path: "/cost-overhead",
    name: "CostOverhead",
    component: CostOverhead
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
