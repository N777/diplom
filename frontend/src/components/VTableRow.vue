<template>
  <v-row no-gutters>
    <v-col class="lesson">{{ dayNumber }}</v-col>
    <VTableCell
      v-for="number in 8"
      :key="number"
      :timetable="getTimeTableForLesson(number)"
    >
    </VTableCell>
    <VTableCellAbsolute>ТЕСТ</VTableCellAbsolute>
  </v-row>
</template>

<style></style>

<script>
import VTableCell from "@/components/VTableCell.vue";
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
    timetable: Array,
    dayNumber: String,
  },
};
</script>

<style scoped>
.v-col {
  overflow: hidden;
  max-width: calc(v-bind(cellWidth) * 1px);
}
</style>
