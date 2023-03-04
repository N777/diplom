<template>
  <router-view />
</template>
<script>
export default {
  methods: {
    addUser() {
      this.$store.commit("increment");
      console.log(this.$store.state.count);
    },
  },
};
</script>
