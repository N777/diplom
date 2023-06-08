<template>
  <v-app>
    <v-app-bar>
      <template v-slot:append>
        <VSearch></VSearch>
        <VLoginModal></VLoginModal>
      </template>
    </v-app-bar>
    <v-main>
      <VTimeTable v-if="timetable" v-bind:timetable="timetable"></VTimeTable>
      <VPrintModal class="print-button"></VPrintModal>
    </v-main>
  </v-app>
</template>

<script>
import VSearch from "./VSearch.vue";
import VTimeTable from "./VTimeTable.vue";
import VLoginModal from "./VLoginModal.vue";
import VPrintModal from "./VPrintModal.vue";

export default {
  data: () => ({ loginDialog: false }),
  components: { VSearch, VTimeTable, VLoginModal, VPrintModal },
  props: ["timetable"],
  name: "VMainPage",
  computed: {},
  created() {
    this.$store.dispatch("getUserInfo");
  },
};
</script>

<style scoped>
.print-button {
  position: fixed;
  bottom: 5px;
  right: 5px;
}
</style>
