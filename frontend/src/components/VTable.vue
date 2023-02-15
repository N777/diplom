<template>
  <div v-for="row in timetable">{{ row.lesson_name }}</div>
  Жопа
  <VTableRow></VTableRow>
</template>

<script>
import VTableRow from "@/components/VTableRow.vue";

export default {
  name: "VTable",
  components: {
    VTableRow,
  },

  props: {
    timetable: Array,
  },
};
</script>

<style scoped></style>
