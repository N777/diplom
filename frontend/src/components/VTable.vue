<template>
  <v-container>
    <v-row no-gutters>
      <p>Неделя номер: {{ weekNumber + 1 }}</p>
    </v-row>
    <v-row no-gutters>
      <v-col class="lesson">Пара Время</v-col>
      <v-col class="lesson" v-for="lesson in 8" :key="lesson"
        >{{ lesson }} пара</v-col
      >
    </v-row>
    <VTableRow
      v-for="day in 7"
      :key="day"
      :timetable="getTimeTableForDay(day)"
      :dayNumber="day"
    ></VTableRow>
  </v-container>
</template>

<style></style>

<script>
import VTableRow from "@/components/VTableRow.vue";

export default {
  name: "VTable",
  components: {
    VTableRow,
  },
  methods: {
    getTimeTableForDay(day) {
      return this.timetable.filter((lesson) => lesson.day === day);
    },
  },
  props: {
    timetable: Array,
    weekNumber: Number,
  },
};
</script>

<style scoped></style>
