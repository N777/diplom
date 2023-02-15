import { createApp } from "vue";
import App from "./App.vue";
import Axios from "axios";

import "./assets/main.css";

import { createStore } from "vuex";

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
  actions: {
    GET_TIMETABLE: async (context) => {
      return Axios.get(
        "http://127.0.0.1:8000/api/timetable/?search=ИВТАПбд-21"
      ).then((res) => {
        context.commit("SET_TODO", res.data);
      });
    },
  },
});

const app = createApp(App);
app.use(store);
app.mount("#app");
