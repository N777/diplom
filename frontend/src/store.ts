import { createStore } from "vuex";
import Axios from "axios";
import { tr } from "vuetify/locale";

export const store = createStore({
  state: {
    token: "",
    isAuth: false,
    count: 0,
    timetable: null,
    groups: [],
  },
  mutations: {
    initAuthStore(state) {
      const token = localStorage.getItem("token");
      if (token) {
        state.token = token;
        state.isAuth = true;
      } else {
        state.isAuth = false;
      }
    },
    setToken(state, token) {
      state.token = token;
      state.isAuth = true;
    },
    removeToken(state) {
      state.token = "";
      state.isAuth = false;
    },
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
      return Axios.get(`api/timetable/?search=${group}`).then((res) => {
        commit("SET_TIMETABLE", res.data);
      });
    },
    GET_GROUPS({ commit }) {
      return Axios.get(`api/group/`).then((res) => {
        commit("SET_GROUPS", res.data);
      });
    },
  },
});
