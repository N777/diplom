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
            v-model="selected"
            :items="search_items"
            label="Favorite Fruits"
            multiple
          >
            <template v-slot:prepend-item>
              <v-list-item title="Select All" @click="toggle">
                <template v-slot:prepend>
                  <v-checkbox-btn :model-value="someSelected"></v-checkbox-btn>
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
    selected: [],
  }),

  computed: {
    ...mapState(["groups", "teachers", "rooms"]),
    search_items() {
      return [...this.groups, ...this.rooms, ...this.teachers];
    },
    allSelected() {
      return this.selected.length === this.search_items.length;
    },
    someSelected() {
      return this.selected.length > 0;
    },
  },

  methods: {
    toggle() {
      if (this.allSelected) {
        this.selected = [];
      } else {
        this.selected = this.search_items.slice();
      }
    },
    getTimetableHTML() {
      axios
        .get("api/print-timetable/", {
          params: { groups: this.selected.toString() },
        })
        .then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));

          // Создайте ссылку для загрузки файла
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", `${this.selected.toString()}.html`); // Замените 'file_name.extension' на имя файла с расширением

          // Добавьте ссылку в DOM и автоматически щелкните по ней, чтобы начать загрузку
          document.body.appendChild(link);
          link.click();

          // Удалите ссылку из DOM
          document.body.removeChild(link);
        });
    },
  },
};
</script>

<style scoped></style>
