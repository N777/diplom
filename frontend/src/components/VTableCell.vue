<template>
  <v-col class="lesson" v-if="timetable">
    <p>
      <router-link
        :to="{ name: 'timetable', params: { timetable: timetable.group_name } }"
        >{{ timetable.group_name }}</router-link
      >
    </p>
    <p>{{ timetable.lesson_name }}</p>
    <p>
      <router-link
        :to="{
          name: 'timetable',
          params: { timetable: timetable.teacher_name },
        }"
        >{{ timetable.teacher_name }}</router-link
      >
    </p>
    <p>
      <router-link
        :to="{
          name: 'timetable',
          params: { timetable: timetable.room_number },
        }"
        >{{ timetable.room_number }}</router-link
      >
    </p>
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
