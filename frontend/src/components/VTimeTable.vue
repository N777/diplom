<template>
  <VTable
    v-if="TIMETABLE"
    v-for="week in 2"
    :timetable="getTimeTableForWeek(week - 1)"
    :weekNumber="week - 1"
  ></VTable>
</template>

<script>
import VTable from "@/components/VTable.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  components: {
    VTable,
    props: ["type", "name"],
  },

  mounted() {
    debugger;
    this.GET_TIMETABLE(this.name);
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
