import { createApp } from "vue";
import App from "./App.vue";
import "@mdi/font/css/materialdesignicons.css";
import "./assets/main.css";

import type { Timetable } from "@/interfaces";

export interface State {
  count: number;
  timetable?: Timetable;
}
axios.defaults.baseURL = "http://127.0.0.1:8000/";
// Create a new store instance.

// Vuetify
import "vuetify/styles";
import { store } from "./store";
import { router } from "./router";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { aliases, mdi } from "vuetify/iconsets/mdi";
import axios from "axios";

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: "mdi",
    aliases,
    sets: {
      mdi,
    },
  },
});

const app = createApp(App);
app.use(store);
app.use(router);
app.use(vuetify);
app.mount("#app");
