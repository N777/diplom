<template>
  <div class="text-center">
    <v-btn icon="mdi-printer" @click="dialog = true"> </v-btn>

    <v-dialog v-model="dialog" width="1024">
      <v-card>
        <v-card-title>
          <span class="text-h5">Печать расписания</span>
        </v-card-title>
        <v-card-text>
          <v-select
            v-model="selectedGroups"
            :items="groups"
            label="Группы"
            multiple
          >
            <template v-slot:prepend-item>
              <v-list-item title="Выбрать все" @click="toggleGroups">
                <template v-slot:prepend>
                  <v-checkbox-btn :model-value="someGroups"></v-checkbox-btn>
                </template>
              </v-list-item>
            </template>
          </v-select>
          <v-select
            v-model="selectedTeachers"
            :items="teachers"
            label="Преподаватели"
            multiple
          >
            <template v-slot:prepend-item>
              <v-list-item title="Выбрать все" @click="toggleTeachers">
                <template v-slot:prepend>
                  <v-checkbox-btn :model-value="someTeachers"></v-checkbox-btn>
                </template>
              </v-list-item>
            </template>
          </v-select>
          <v-select
            v-model="selectedRooms"
            :items="rooms"
            label="Аудитории"
            multiple
          >
            <template v-slot:prepend-item>
              <v-list-item title="Выбрать все" @click="toggleRooms">
                <template v-slot:prepend>
                  <v-checkbox-btn :model-value="someRooms"></v-checkbox-btn>
                </template>
              </v-list-item>
            </template>
          </v-select>
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" block @click="getTimetableHTML">Печать</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";

export default {
  name: "VPrintModal",
  data: () => ({
    dialog: false,
    selectedGroups: [],
    selectedTeachers: [],
    selectedRooms: [],
  }),

  computed: {
    ...mapState(["groups", "teachers", "rooms"]),
    someGroups() {
      return this.selectedGroups.length > 0;
    },
    someTeachers() {
      return this.selectedTeachers.length > 0;
    },
    someRooms() {
      return this.selectedRooms.length > 0;
    },
  },

  methods: {
    toggleGroups() {
      if (this.selectedGroups.length === this.groups.length) {
        this.selectedGroups = [];
      } else {
        this.selectedGroups = this.groups.slice();
      }
    },
    toggleTeachers() {
      if (this.selectedTeachers.length === this.teachers.length) {
        this.selectedTeachers = [];
      } else {
        this.selectedTeachers = this.teachers.slice();
      }
    },
    toggleRooms() {
      if (this.selectedRooms.length === this.rooms.length) {
        this.selectedRooms = [];
      } else {
        this.selectedRooms = this.rooms.slice();
      }
    },
    getTimetableHTML() {
      const selectedItems = [
        ...this.selectedGroups,
        ...this.selectedRooms,
        ...this.selectedTeachers,
      ];
      if (selectedItems.length === 0) {
        return;
      }
      axios
        .get("api/print-timetable/", {
          params: { names: selectedItems.toString() },
        })
        .then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", `${selectedItems.toString()}.html`);
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
          this.dialog = false;
        });
    },
  },
};
</script>

<style scoped></style>
