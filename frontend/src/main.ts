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
    component: () => import("@/components/VTimeTable.vue"),
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
  },
  mutations: {
    increment(state) {
      state.count++;
    },
    SET_TODO: (state, payload) => {
      state.timetable = payload;
    },
  },
  getters: {
    TIMETABLE(state) {
      return state.timetable;
    },
  },
  actions: {
    GET_TIMETABLE({ commit }, { group }) {
      return Axios.get(
        `http://127.0.0.1:8000/api/timetable/?search=${group}`
      ).then((res) => {
        commit("SET_TODO", res.data);
      });
    },
  },
});

const app = createApp(App);
app.use(store);
app.use(router);
app.mount("#app");
