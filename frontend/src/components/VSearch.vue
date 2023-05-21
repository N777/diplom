<template>
  <v-autocomplete
    v-model="select"
    v-model:search="search"
    :items="groups"
    hide-no-data
    hide-details
    label="Поиск"
    variant="underlined"
    @keydown.enter="find"
    style="min-width: 80vw"
  ></v-autocomplete>
</template>

<script>
import { mapActions, mapState, mapGetters } from "vuex";

export default {
  name: "VSearch",
  data: () => ({
    items: [],
    select: null,
    search: null,
    loaded: false,
    loading: false,
  }),
  mounted() {
    this.GET_GROUPS();
    this.GET_TEACHERS();
    this.GET_ROOMS();
    this.GET_LESSONS();
    this.GET_LESSONS_TIMES();
  },
  computed: {
    ...mapGetters(["GROUPS"]),
    ...mapState(["groups"]),
  },
  watch: {
    search(val) {
      if (this.GROUPS.includes(val)) {
        this.select = val;
        this.find();
      }
    },
  },
  methods: {
    ...mapActions(["GET_GROUPS", "GET_TEACHERS", "GET_ROOMS", "GET_LESSONS", "GET_LESSONS_TIMES"]),
    find() {
      this.$router.push({
        name: "timetable",
        params: { timetable: this.select },
      });
    },
  },
};
</script>

<style scoped></style>
