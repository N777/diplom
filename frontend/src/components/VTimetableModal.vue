<template>
  <v-row no-gutters justify="center">
    <v-dialog v-model="dialog" persistent width="1024">
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
            <v-text-field
              v-model="lesson.lesson_name"
              label="Занятие"
            ></v-text-field>
            <v-text-field
              v-model="lesson.group_name"
              label="Группа"
            ></v-text-field>
            <v-text-field
              v-model="lesson.teacher_name"
              label="Преподаватель"
            ></v-text-field>
            <v-text-field
              v-model="lesson.room_number"
              label="Аудитория"
            ></v-text-field>
            <v-select
              v-model="days[lesson.day]"
              :items="days"
              :rules="[(v) => !!v || 'Item is required']"
              label="День"
            ></v-select>
            <v-select
              v-model="weeks[lesson.week]"
              :items="weeks"
              :rules="[(v) => !!v || 'Item is required']"
              label="Неделя"
            ></v-select>
            <v-text-field
              v-model="lesson.lesson_number"
              label="Пара №"
            ></v-text-field>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
            Закрыть
          </v-btn>
          <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  name: "VTimetableModal",
  data() {
    return {
      dialog: false,
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
    letter_day: function () {
      return this.getDayName(this.lesson.day);
    },
  },
  methods: {
    getDayName(number) {
      return this.days[number];
    },
  },
  props: {
    lesson: Object,
  },
};
</script>

<style scoped></style>
