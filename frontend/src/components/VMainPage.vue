<template>
  <v-app>
    <v-app-bar>
      <template v-slot:append>
        <VSearch></VSearch>
        <VLoginModel></VLoginModel>
      </template>
    </v-app-bar>
    <v-main>
      <VTimeTable v-if="timetable" v-bind:timetable="timetable"></VTimeTable>
    </v-main>
  </v-app>
</template>

<script>
import VSearch from "./VSearch.vue";
import VTimeTable from "./VTimeTable.vue";
import VLoginModel from "./VLoginModel.vue";

export default {
  data: () => ({loginDialog: false}),
  components: {VSearch, VTimeTable, VLoginModel},
  props: ["timetable"],
  name: "VMainPage",
  computed: {},
  created() {
    this.$store.dispatch("getUserInfo");
  }
};
</script>

<style scoped></style>
