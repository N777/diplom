<template>
  <v-autocomplete
    v-model="select"
    v-model:search="search"
    :items="groups"
    hide-no-data
    hide-details
    label="Поиск"
    @keydown.enter="find"
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
    ...mapActions(["GET_GROUPS"]),
    find() {
      this.$router.push({
        name: "timetable",
        params: { timetable: this.select },
      });
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
