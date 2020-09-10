import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";

import VueLodash from "vue-lodash";
import lodash from "lodash";

import "prismjs";
import "prismjs/themes/prism-tomorrow.css";
import "prismjs/components/prism-powershell.min";
import "prismjs/components/prism-markup.min";
import "prismjs/plugins/autolinker/prism-autolinker.min";
import "prismjs/plugins/autolinker/prism-autolinker.css";
import Prism from "vue-prism-component";

import InfoCard from "@/components/InfoCard.vue";
import WarningCard from "@/components/WarningCard.vue";

Vue.config.productionTip = false;

Vue.component("prism", Prism);
Vue.component("info-card", InfoCard);
Vue.component("warning-card", WarningCard);
Vue.use(VueLodash, { lodash: lodash });

new Vue({
  vuetify,
  router,
  render: (h) => h(App),
}).$mount("#app");
