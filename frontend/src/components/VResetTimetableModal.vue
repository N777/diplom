<template>
  <v-dialog v-model="dialog" persistent width="600">
    <template v-slot:activator="{ props }">
      <v-btn v-bind="props">Сбросить</v-btn>
    </template>
    <v-card>
      <v-card-title class="text-h5"> Подтверждение </v-card-title>
      <v-card-text
        ><p>Вы уверены, что хотите сбросить расписание?</p>
        <p>
          Это приведёт к удалению расписанию всех групп и преподавателей и
          получению нового с официального расписание УлГТУ.
        </p>
        <p><b>Внимание!</b> Процесс может занять до 5 минут</p>
      </v-card-text>
      <div v-if="hideButtons" style="margin: auto; min-height: 50px">
        <v-progress-circular
          color="primary"
          indeterminate
        ></v-progress-circular>
      </div>
      <v-card-actions v-if="!hideButtons">
        <v-spacer></v-spacer>
        <v-btn color="green-darken-1" variant="text" @click="dialog = false">
          Нет
        </v-btn>
        <v-btn color="green-darken-1" variant="text" @click="resetTimetable()">
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
  name: "VResetTimetableModal",
  methods: {
    ...mapActions(["GET_TIMETABLE"]),
    resetTimetable: function () {
      this.hideButtons = true;
      Axios.post(`api/reset-timetable/`).then((res) => {
        this.GET_TIMETABLE(this.$route.params.timetable);
        this.dialog = false;
        console.log(res);
      });
    },
  },
  data() {
    return {
      hideButtons: false,
      dialog: false,
    };
  },
};
</script>

<style scoped></style>
