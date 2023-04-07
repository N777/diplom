<template>
  <v-col class="lesson" v-if="timetable">
    <p>
      <router-link
        :to="{ name: 'timetable', params: { timetable: timetable.group } }"
        >{{ timetable.group }}</router-link
      >
    </p>
    <p>{{ timetable.lesson }}</p>
    <p>
      <router-link
        :to="{
          name: 'timetable',
          params: { timetable: timetable.teacher },
        }"
        >{{ timetable.teacher }}</router-link
      >
    </p>
    <p>
      <router-link
        :to="{
          name: 'timetable',
          params: { timetable: timetable.room },
        }"
        >{{ timetable.room }}</router-link
      >
    </p>

    <v-row v-if="isAuth" class="edit" no-gutters>
      <VTimetableModal :lesson="timetable"></VTimetableModal>
      <VDeleteTimetableModal
        :timetable_id="timetable.id"
      ></VDeleteTimetableModal>
    </v-row>
  </v-col>
  <v-col
    v-else
    v-on:click="log"
    class="lesson d-flex align-center justify-center"
  >
    <v-btn size="x-small" v-if="isAuth" icon="mdi-plus" variant="plain"></v-btn>
  </v-col>
</template>

<style>
.edit {
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
import { mapState } from "vuex";
import VDeleteTimetableModal from "./VDeleteTimetableModal.vue";
import VTimetableModal from "@/components/VTimetableModal.vue";

export default {
  name: "VTableCell",
  components: { VDeleteTimetableModal, VTimetableModal },
  props: {
    timetable: Object,
  },
  methods: {
    log: function () {
      console.log("Нет доступа");
    },
  },
  computed: {
    ...mapState(["isAuth"]),
  },
};
</script>

<style scoped></style>
