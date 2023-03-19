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
    <v-row class="edit" no-gutters>
      <v-btn size="small" v-if="isAuth" icon="mdi-pencil-outline" variant="plain"></v-btn>
    </v-row>

  </v-col>
  <v-col v-on:click="log" class="lesson d-flex align-center justify-center" v-else>
      <v-btn size="x-small" v-if="isAuth" icon="mdi-plus" variant="plain"></v-btn>
  </v-col>
</template>

<style>
.edit{
  position: absolute;
  bottom: 0;
  right: 0;
}
.lesson {
  border: 1px solid black;
  position: relative;
}
</style>

<script>
import {mapState} from "vuex";

export default {
  name: "VTableCell",
  props: {
    timetable: Object,
  },
  methods:{
    log: function () {
      console.log("Нет доступа")
    }
  },
  computed:{
    ...mapState(['isAuth'])
  },
};
</script>

<style scoped></style>
