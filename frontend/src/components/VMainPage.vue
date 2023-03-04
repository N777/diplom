<template>
  <VSearch></VSearch>
  <router-view />
</template>

<script>
import VSearch from "./VSearch.vue";

export default {
  components: { VSearch },
  name: "VMainPage",
};
</script>

<style scoped></style>
