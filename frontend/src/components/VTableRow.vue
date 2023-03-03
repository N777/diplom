<template>
  <v-row no-gutters>
    <v-col class="lesson">{{ getDayName(dayNumber - 1) }}</v-col>
    <VTableCell
      v-for="number in 8"
      :key="number"
      :timetable="getTimeTableForLesson(number)"
    >
    </VTableCell>
  </v-row>
</template>

<style></style>

<script>
import VTableCell from "@/components/VTableCell.vue";

export default {
  name: "VTableRow",
  components: { VTableCell },
  methods: {
    getTimeTableForLesson(number) {
      const lessons = this.timetable.filter(
        (lesson) => lesson.lesson_number === number
      );
      return lessons ? lessons[0] : null;
    },
    getDayName(number) {
      const days = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье",
      ];
      return days[number];
    },
  },
  props: {
    timetable: Array,
    dayNumber: Number,
  },
};
</script>

<style scoped></style>
