<template>
  <main>
    <div>
      <VTable
        v-if="TIMETABLE"
        v-for="week in 2"
        :timetable="getTimeTableForWeek(week - 1)"
        :weekNumber="week - 1"
      ></VTable>
    </div>
  </main>
</template>
<script>
import VTable from "@/components/VTable.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  components: {
    VTable,
    props: {
      type: String,
      name: String,
    },
  },

  mounted() {
    debugger;
    this.GET_TIMETABLE(this.$route.params.name);
  },
  computed: {
    ...mapGetters(["TIMETABLE"]),
  },
  methods: {
    ...mapActions(["GET_TIMETABLE"]),
    getTimeTableForWeek(week) {
      return this.TIMETABLE.filter((lesson) => lesson.week === week);
    },
    addUser() {
      this.$store.commit("increment");
      console.log(this.$store.state.count);
    },
  },
};
</script>
