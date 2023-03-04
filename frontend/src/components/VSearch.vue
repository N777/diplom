<template>
  <v-icon icon="mdi-vuetify" size="x-large"></v-icon>
  <v-autocomplete
    :items="groups"
    label="Поиск"
    @keydown.enter="search"
  ></v-autocomplete>
</template>

<script>
import { mapActions, mapState, mapGetters } from "vuex";

export default {
  name: "VSearch",
  data: () => ({
    items: [],
    select: null,
    loaded: false,
    loading: false,
  }),
  mounted() {
    this.GET_GROUPS();
  },
  computed: {
    ...mapGetters(["GROUPS"]),
    ...mapState(["groups"]),
  },

  methods: {
    ...mapActions(["GET_GROUPS"]),
    search() {
      this.$router.push("timetable");
    },
  },
};
</script>

<style scoped>
.v-text-field {
  margin: 10px auto;
  max-width: 90vw;
}
</style>
