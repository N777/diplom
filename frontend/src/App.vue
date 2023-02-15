<template>
  <main>
    <div>
      <VTable :timetable="TIMETABLE"></VTable>
      <VTable></VTable>
    </div>
  </main>
</template>

<script>
import VTable from "@/components/VTable.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  components: { VTable },

  data() {
    return {
      users: [
        { name: "qwe", age: 12 },
        { name: "qw8", age: 15 },
        { name: "qw7", age: 19 },
      ],
    };
  },
  mounted() {
    this.GET_TIMETABLE();
  },
  computed: {
    ...mapGetters(["TIMETABLE"]),
  },
  methods: {
    ...mapActions(["GET_TIMETABLE"]),
    getTimeTableForWeek(week) {
      debugger;
      return this.TIMETABLE.filter((lesson) => lesson.week === week);
    },
    addUser() {
      this.$store.commit("increment");
      console.log(this.$store.state.count);
      this.users.push({
        name: "Rtrd",
        age: 15,
      });
    },
  },
};
</script>
