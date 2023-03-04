import { createApp } from "vue";
import App from "./App.vue";
import Axios from "axios";
import { createRouter, createWebHistory } from "vue-router";

import "./assets/main.css";

import { createStore } from "vuex";
import type { Timetable } from "@/interfaces";

export interface State {
  count: number;
  timetable?: Timetable;
}

const routes = [
  {
    path: "/:type/:name",
    name: "timetable",
    component: () => import("@/components/VTimeTable.vue"),
    props: true,
  },
  {
    path: "/",
    component: () => import("@/components/VMainPage.vue"),
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes, // short for `routes: routes`
});

// Create a new store instance.
const store = createStore({
  state: {
    count: 0,
    timetable: null,
    groups: [],
  },
  mutations: {
    increment(state) {
      state.count++;
    },
    SET_TIMETABLE: (state, payload) => {
      state.timetable = payload;
    },
    SET_GROUPS: (state, payload) => {
      state.groups = payload;
    },
  },
  getters: {
    TIMETABLE(state) {
      return state.timetable;
    },
    GROUPS(state) {
      return state.groups;
    },
  },
  actions: {
    GET_TIMETABLE({ commit }, group) {
      return Axios.get(
        `http://127.0.0.1:8000/api/timetable/?search=${group}`
      ).then((res) => {
        commit("SET_TIMETABLE", res.data);
      });
    },
    GET_GROUPS({ commit }) {
      return Axios.get(`http://127.0.0.1:8000/api/group/`).then((res) => {
        commit("SET_GROUPS", res.data);
      });
    },
  },
});

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { aliases, mdi } from "vuetify/iconsets/mdi";

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
