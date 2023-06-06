<template>
  <v-row no-gutters>
    <v-col class="lesson">{{ dayName }}</v-col>
    <VTableCell
      v-for="number in 8"
      :key="number"
      :lesson_number="number"
      :day="dayName"
      :week="week"
      :timetable="getTimeTableForLesson(number)"
    >
    </VTableCell>
    <!--    <VTableCellAbsolute>ТЕСТ</VTableCellAbsolute>-->
  </v-row>
</template>

<script>
import VTableCell from "./VTableCell.vue";
import { mapState } from "vuex";
import VTableCellAbsolute from "./VTableCellAbsolute.vue";

export default {
  name: "VTableRow",
  components: { VTableCellAbsolute, VTableCell },
  methods: {
    getTimeTableForLesson(number) {
      const lessons = this.timetable.filter(
        (lesson) => lesson.lesson_number === number
      );
      return lessons ? lessons[0] : null;
    },
  },
  computed: {
    ...mapState(["cellWidth"]),
  },
  props: {
    week: Number,
    timetable: Array,
    dayName: String,
  },
};
</script>

<style scoped>
.v-col {
  overflow: hidden;
  max-width: calc(v-bind(cellWidth) * 1px);
}
</style>
