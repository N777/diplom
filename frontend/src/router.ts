import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/:timetable",
    name: "timetable",
    component: () => import("@/components/VMainPage.vue"),
    props: true,
  },
  {
    path: "/",
    component: () => import("@/components/VMainPage.vue"),
    props: true,
  },
];

export const router = createRouter({
  history: createWebHistory(),
  routes, // short for `routes: routes`
});
