<template>
  <v-dialog v-model="dialog" persistent width="auto">
    <template v-slot:activator="{ props }">
      <v-btn
        size="small"
        icon="mdi-alpha-x"
        variant="plain"
        v-bind="props"
      ></v-btn>
    </template>
    <v-card>
      <v-card-title class="text-h5"> Подтверждение </v-card-title>
      <v-card-text>Вы уверены, что хотите удалить занятие?</v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="green-darken-1" variant="text" @click="dialog = false">
          Нет
        </v-btn>
        <v-btn
          color="green-darken-1"
          variant="text"
          @click="deleteTimetable(timetable_id)"
        >
          Да
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import Axios from "axios";
import { mapActions } from "vuex";

export default {
  name: "VDeleteTimetableModal",
  props: {
    timetable_id: Number,
  },
  methods: {
    ...mapActions(["GET_TIMETABLE"]),
    deleteTimetable: function (id) {
      Axios.delete(`api/timetable/${id}/`).then((res) => {
        this.$store.state.timetable = this.$store.state.timetable.filter(
          function (f) {
            return f.id !== id;
          }
        );
        this.GET_TIMETABLE(this.$route.params.timetable);
        this.dialog = false;
        console.log(res);
      });
    },
  },
  data() {
    return {
      dialog: false,
    };
  },
};
</script>

<style scoped></style>
