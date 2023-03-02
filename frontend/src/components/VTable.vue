<template>
  <!--  <div v-for="row in timetable">{{ row.lesson_name }}</div>-->
  <p>Неделя номер: {{ weekNumber + 1 }}</p>
  <div class="week">
    <div class="day">
      <div class="lesson">Пара Время</div>
      <div class="lesson" v-for="lesson in 8">{{ lesson }} пара</div>
    </div>
    <VTableRow
      v-for="day in 7"
      :key="day"
      :timetable="getTimeTableForDay(day)"
      :dayNumber="day"
    ></VTableRow>
  </div>
</template>

<style>
.week {
  display: flex;
  margin: 10px;
  flex-direction: column;
}
</style>

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
