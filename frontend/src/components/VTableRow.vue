<template>
  <v-row no-gutters>
    <v-col class="lesson">{{ dayNumber }}</v-col>
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
  },
  props: {
    timetable: Array,
    dayNumber: Number,
  },
};
</script>

<style scoped></style>
