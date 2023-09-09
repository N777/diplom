<template>
  <VTable
    v-if="TIMETABLE"
    v-for="week in [1, 0]"
    :timetable="getTimeTableForWeek(week)"
    :weekNumber="week"
  ></VTable>
</template>

<script>
import VTable from "./VTable.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  components: {
    VTable,
  },
  props: ["timetable"],
  mounted() {
    this.GET_TIMETABLE(this.timetable);
  },
  watch: {
    // при изменениях маршрута запрашиваем данные снова
    $route(to, from) {
      this.GET_TIMETABLE(to.params.timetable);
    },
  },
  computed: {
    ...mapGetters(["TIMETABLE"]),
  },
  methods: {
    ...mapActions(["GET_TIMETABLE"]),
    getTimeTableForWeek(week) {
      return this.TIMETABLE.filter((lesson) => lesson.week === week);
    },
  },
};
</script>

<style scoped></style>
