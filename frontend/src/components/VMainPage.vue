<template>
  <VSearch></VSearch>
  <VTimeTable v-if="timetable" v-bind:timetable="timetable"></VTimeTable>
</template>

<script>
import VSearch from "./VSearch.vue";
import VTimeTable from "./VTimeTable.vue";

export default {
  components: { VSearch, VTimeTable },
  props: ["timetable"],
  name: "VMainPage",
  computed: {},
};
</script>

<style scoped></style>
