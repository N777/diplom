<template>
  <router-view />
</template>
<script>
import { mapMutations, mapState } from "vuex";
import axios from "axios";

export default {
  created() {
    this.$store.commit("initAuthStore");
    if (this.token) {
      axios.defaults.headers.common["Authorization"] = "Token " + this.token;
    }
  },
  computed: {
    ...mapState(["token"]),
  },
  methods: {
    addUser() {
      this.$store.commit("increment");
      console.log(this.$store.state.count);
    },
  },
};
</script>
