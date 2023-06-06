<template>
  <v-container>
    <v-row no-gutters>
      <p>Неделя номер: {{ weekNumber + 1 }}</p>
    </v-row>
    <v-row no-gutters>
      <v-col ref="basecell" class="lesson">Пара Время</v-col>
      <v-col class="lesson" v-for="lesson in lessonsTimes" :key="lesson"
        >{{ lesson.id }} пара <br />
        {{ lesson.start_time }}-{{ lesson.end_time }}
      </v-col>
    </v-row>
    <VTableRow
      v-for="day in weekdays"
      :key="day"
      :week="weekNumber"
      :timetable="getTimeTableForDay(day)"
      :dayName="day"
    ></VTableRow>
  </v-container>
</template>

<style></style>

<script>
import VTableRow from "./VTableRow.vue";
import { mapMutations, mapState } from "vuex";
import { days } from "@/constants";

export default {
  name: "VTable",
  mounted() {
    this.setCellWidth(this.$refs.basecell.$el.offsetWidth);
  },
  components: {
    VTableRow,
  },
  methods: {
    ...mapMutations(["setCellWidth"]),
    getTimeTableForDay(day) {
      return this.timetable.filter((lesson) => lesson.day === day);
    },
  },
  computed: {
    ...mapState(["lessonsTimes"]),
    weekdays() {
      return days;
    },
  },
  props: {
    timetable: Array,
    weekNumber: Number,
  },
};
</script>

<style scoped></style>
