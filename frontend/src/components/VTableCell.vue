<template>
  <v-col class="lesson" v-if="timetable">
    <div style="padding: 0.2rem">
      <p v-if="timetable?.group">
        <router-link
          :to="{ name: 'timetable', params: { timetable: timetable.group } }"
          >{{ timetable.group }}
        </router-link>
      </p>
      <p>{{ timetable.lesson }}</p>
      <p v-if="timetable?.teacher">
        <router-link
          :to="{
            name: 'timetable',
            params: { timetable: timetable.teacher },
          }"
          >{{ timetable.teacher }}
        </router-link>
      </p>
      <p>
        <router-link
          :to="{
            name: 'timetable',
            params: { timetable: timetable.room },
          }"
          >{{ timetable.room }}
        </router-link>
      </p>
    </div>
    <div v-if="isAuth" class="edit">
      <VTimetableModal :lesson="timetable" :edit-mode="true"></VTimetableModal>
      <VDeleteTimetableModal
        :timetable_id="timetable.id"
      ></VDeleteTimetableModal>
    </div>
  </v-col>
  <v-col
    v-on:click="log"
    v-else
    class="lesson d-flex align-center justify-center"
  >
    <VTimetableModal
      :lesson="newTimetable"
      :edit-mode="false"
    ></VTimetableModal>
  </v-col>
</template>

<style>
.edit {
  display: flex;
  justify-content: flex-end;
}

.lesson {
  border: 1px solid black;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
}
</style>

<script>
import { mapState } from "vuex";
import VDeleteTimetableModal from "./VDeleteTimetableModal.vue";
import VTimetableModal from "./VTimetableModal.vue";

export default {
  name: "VTableCell",
  components: { VDeleteTimetableModal, VTimetableModal },
  props: {
    day: String,
    lesson_number: Number,
    week: Number,
    timetable: Object,
  },
  methods: {
    log: function () {
      debugger;
      console.log("Нет доступа");
    },
  },
  computed: {
    ...mapState(["isAuth"]),
    newTimetable() {
      return {
        day: this.day,
        lesson_number: this.lesson_number,
        week: this.week,
      };
    },
  },
};
</script>

<style scoped></style>
