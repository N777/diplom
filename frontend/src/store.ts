import { createStore } from "vuex";
import Axios from "axios";
import { tr } from "vuetify/locale";
import axios from "axios";

export const store = createStore({
  state: {
    token: "",
    userInfo: null,
    isAuth: false,
    cellWidth: 0,
    count: 0,
    timetable: null,
    groups: [],
    teachers: [],
    rooms: [],
    lessons: [],
    lessonsTimes: [],
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
    SET_ROOMS: (state, payload) => {
      state.rooms = payload;
    },
    SET_TEACHERS: (state, payload) => {
      state.teachers = payload;
    },
    SET_LESSONS: (state, payload) => {
      state.lessons = payload;
    },
    SET_LESSONS_TIMES: (state, payload) => {
      state.lessonsTimes = payload;
    },
    setUserInfo: (state, payload) => {
      state.userInfo = payload;
    },
    setCellWidth: (state, payload) => {
      state.cellWidth = payload;
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
    addToken({ commit }, token) {
      commit("setToken", token);
      axios.defaults.headers.common["Authorization"] = "Token " + token;
      localStorage.setItem("token", token);
    },
    deleteToken({ commit }) {
      commit("removeToken");
      localStorage.removeItem("token");
      delete axios.defaults.headers.common["Authorization"];
    },
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
    GET_TEACHERS({ commit }) {
      return Axios.get(`api/teacher/`).then((res) => {
        commit("SET_TEACHERS", res.data);
      });
    },
    GET_ROOMS({ commit }) {
      return Axios.get(`api/room/`).then((res) => {
        commit("SET_ROOMS", res.data);
      });
    },
    GET_LESSONS({ commit }) {
      return Axios.get(`api/lesson/`).then((res) => {
        commit("SET_LESSONS", res.data);
      });
    },
    GET_LESSONS_TIMES({ commit }) {
      return Axios.get(`api/lessons-times/`).then((res) => {
        commit("SET_LESSONS_TIMES", res.data);
      });
    },
    getUserInfo({ commit }) {
      return Axios.get(`auth/users/me/`).then((res) => {
        commit("setUserInfo", res.data);
      });
    },
  },
});
