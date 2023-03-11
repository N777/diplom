<template>
  <VSearch></VSearch>
  <VTimeTable
    v-if="this.$route.params?.timetable"
    timetable="this.$route.params?.timetable"
  ></VTimeTable>
</template>

<script>
import VSearch from "./VSearch.vue";
import VTimeTable from "./VTimeTable.vue";

export default {
  components: { VSearch, VTimeTable },
  name: "VMainPage",
  computed: {},
};
</script>

<style scoped></style>
