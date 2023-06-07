<template>
  <v-form ref="form" fast-fail>
    <v-dialog v-model="dialog" width="1024">
      <template #activator="{ props }">
        <v-btn
          size="small"
          variant="plain"
          v-bind="props"
          :icon="editMode ? 'mdi-pencil-outline' : 'mdi-plus'"
        />
      </template>
      <v-card>
        <v-card-title>
          <span v-if="editMode" class="text-h5">Редактирование</span>
          <span v-else class="text-h5">Создание</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-col v-if="!editMode">
              <v-btn-toggle
                v-model="modalData.lesson_type"
                rounded="1"
                color="blue"
                group
                variant="plain"
              >
                <v-btn :value="types.Lesson"> Занятие </v-btn>
                <v-btn :value="types.Event"> Мероприятие </v-btn>
              </v-btn-toggle>
            </v-col>
            <v-text-field
              v-if="isTypeEvent"
              v-model="modalData.lesson"
              label="Название мероприятия"
            />
            <v-autocomplete
              v-if="!isTypeEvent"
              v-model="modalData.lesson"
              :items="lessons"
              label="Название занятия"
            />
            <v-autocomplete
              v-if="!isTypeEvent"
              v-model="modalData.group"
              :items="groups"
              label="Группа"
            />
            <v-autocomplete
              v-if="!isTypeEvent"
              v-model="modalData.teacher"
              :items="teachers"
              label="Преподаватель"
            />
            <v-autocomplete
              v-model="modalData.room"
              :items="rooms"
              :rules="[(v) => !!v || 'Аудитория']"
              required
              label="Аудитория"
            />
            <v-autocomplete
              v-if="!isTypeEvent"
              v-model="modalData.day"
              :items="days"
              label="День"
            />
            <v-select
              v-if="!isTypeEvent"
              v-model="weeks[modalData.week]"
              :items="weeks"
              label="Неделя"
            />
            <v-text-field
              v-if="isTypeEvent"
              v-model="modalData.date"
              type="date"
              label="Начало"
            />
            <v-text-field
              v-if="isTypeEvent"
              v-model="modalData.start_time"
              type="time"
              label="Начало"
            />
            <v-text-field
              v-if="isTypeEvent"
              v-model="modalData.end_time"
              type="time"
              label="Конец"
            />
            <v-text-field
              v-if="!isTypeEvent"
              v-model.number="modalData.lesson_number"
              type="number"
              label="Пара №"
              :rules="[(v) => (0 < v && v < 9) || 'Введена некорректная пара']"
            />
            <v-switch v-model="modalData.once" label="Один раз"></v-switch>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
            Закрыть
          </v-btn>
          <v-btn color="blue-darken-1" variant="text" @click="validate">
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-form>
</template>

<script>
import { mapActions, mapState } from "vuex";
import { reactive } from "vue";
import { TimetableType } from "../enums";
import TimetableApi from "../requests";

export default {
  name: "VTimetableModal",
  data() {
    return {
      types: TimetableType,
      type: TimetableType.Lesson,
      modalData: reactive({ ...this.lesson }),
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
    ...mapState(["groups", "teachers", "rooms", "lessons", "timetable"]),
    isTypeEvent() {
      return this.modalData.lesson_type === this.types.Event;
    },
  },
  methods: {
    ...mapActions(["GET_TIMETABLE"]),
    async validate() {
      const { valid } = await this.$refs.form.validate();
      if (valid) await this.save();
    },
    async save() {
      if (this.editMode) {
        await TimetableApi.editTimetable(this.modalData.id, this.modalData);
        const i = this.timetable.indexOf(this.lesson);
        this.timetable[i] = this.modalData;
      } else {
        let response;
        if (this.isTypeEvent) {
          response = await TimetableApi.createTimetableEvent(this.modalData);
        } else {
          response = await TimetableApi.createTimetableLesson(this.modalData);
        }
        debugger;
        await this.GET_TIMETABLE(this.$route.params.timetable);
      }

      this.dialog = false;
    },
  },
  props: {
    lesson: Object,
    editMode: Boolean,
  },
};
</script>

<style scoped></style>
