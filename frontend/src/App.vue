<template>
  <main>
    <VSearch></VSearch>
    <router-view />
  </main>
</template>
<script>
import VSearch from "@/components/VSearch.vue";

export default {
  components: { VSearch },

  methods: {
    addUser() {
      this.$store.commit("increment");
      console.log(this.$store.state.count);
    },
  },
};
</script>
