<template>
  <v-col class="lesson" v-if="timetable">
    {{ timetable.lesson_name }}
  </v-col>
  <v-spacer class="lesson" v-else></v-spacer>
</template>

<style>
.lesson {
  border: 1px solid black;
}
</style>

<script>
export default {
  name: "VTableCell",
  props: {
    timetable: Object,
  },
};
</script>

<style scoped></style>
