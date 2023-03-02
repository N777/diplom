<template>
  <main>
    <router-view />
  </main>
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
