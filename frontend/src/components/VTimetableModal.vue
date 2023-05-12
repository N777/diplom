<template>
  <v-row no-gutters justify="center">
    <v-form fast-fail v-model="form">
      <v-dialog v-model="dialog" width="1024">
        <template v-slot:activator="{ props }">
          <v-btn
            size="small"
            icon="mdi-pencil-outline"
            variant="plain"
            v-bind="props"
          ></v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="text-h5">Редактирование</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-autocomplete
                v-model="modalData.lesson"
                :items="lessons"
                label="Занятие"
              ></v-autocomplete>
              <v-autocomplete
                v-model="modalData.group"
                :items="groups"
                label="Группа"
              ></v-autocomplete>
              <v-autocomplete
                v-model="modalData.teacher"
                :items="teachers"
                label="Преподаватель"
              ></v-autocomplete>
              <v-autocomplete
                v-model="modalData.room"
                :items="rooms"
                label="Аудитория"
              ></v-autocomplete>
              <v-autocomplete
                v-model="modalData.day"
                :items="days"
                label="День"
              ></v-autocomplete>
              <v-select
                v-model="weeks[modalData.week]"
                :items="weeks"
                label="Неделя"
              ></v-select>
              <v-text-field
                v-model="modalData.lesson_number"
                label="Пара №"
                :rules="[
                  (v) => (0 < v && v < 8) || 'Введена некорректная пара',
                ]"
                v-on:change="
                  modalData.lesson_number = parseFloat(modalData.lesson_number)
                "
              ></v-text-field>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
              Закрыть
            </v-btn>
            <v-btn
              color="blue-darken-1"
              variant="text"
              @click="save"
              :disabled="!form"
            >
              Сохранить
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-form>
  </v-row>
</template>

<script>
import { mapState } from "vuex";
import { reactive } from "vue";

export default {
  name: "VTimetableModal",
  data() {
    return {
      modalData: reactive({ ...this.lesson }),
      dialog: false,
      form: true,
      days: [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье",
      ],
      weeks: ["Чётная", "Нечётная"],
    };
  },
  computed: {
    ...mapState(["groups", "teachers", "rooms", "lessons", "timetable"]),
  },
  methods: {
    save() {
      const i = this.timetable.indexOf(this.lesson);
      this.timetable[i] = this.modalData;
      this.dialog = false;
    },
  },
  props: {
    lesson: Object,
  },
};
</script>

<style scoped></style>
