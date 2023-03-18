<template>
  <VSearch></VSearch>

  <VLoginModel v-bind:open-dialog="loginDialog"></VLoginModel>
  <VTimeTable v-if="timetable" v-bind:timetable="timetable"></VTimeTable>
</template>

<script>
import VSearch from "./VSearch.vue";
import VTimeTable from "./VTimeTable.vue";
import VLoginModel from "./VLoginModel.vue";

export default {
  data: () => ({ loginDialog: false }),
  components: { VSearch, VTimeTable, VLoginModel },
  props: ["timetable"],
  name: "VMainPage",
  computed: {},
};
</script>

<style scoped></style>
