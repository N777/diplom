import { createApp } from "vue";
import App from "./App.vue";
import Axios from "axios";

import "./assets/main.css";

import { createStore } from "vuex";
import type { Timetable } from "@/interfaces";
import { state } from "vue-tsc/out/shared";

export interface State {
  count: number;
  timetable?: Timetable;
}

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
    GET_TIMETABLE({ commit }) {
      return Axios.get(
        "http://127.0.0.1:8000/api/timetable/?search=ИВТАПбд-21"
      ).then((res) => {
        commit("SET_TODO", res.data);
      });
    },
  },
});

const app = createApp(App);
app.use(store);
app.mount("#app");
