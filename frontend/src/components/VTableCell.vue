<template>
  <div class="lesson">
    <div v-if="timetable">
      {{timetable.lesson_name}}
    </div>
  </div>

</template>

<style>
.lesson {
  height: 100px;
  border: 1px solid white;
  min-width: calc(100% /9) ;
  margin: 2px;
}
</style>

<script>
export default {
  name: "VTableCell",
  props: {
    timetable: Object,
  },
};
</script>

<style scoped></style>
