<template>
  <v-icon icon="mdi-vuetify" size="x-large"></v-icon>
  <v-autocomplete
    v-model="select"
    v-model:search="search"
    :loading="loading"
    :items="items"
    class="mx-4"
    density="comfortable"
    hide-no-data
    hide-details
    label="What state are you from?"
    style="max-width: 300px"
  ></v-autocomplete>
</template>

<script>
export default {
  name: "VSearch",
  data: () => ({
    loaded: false,
    loading: false,
  }),
  methods: {
    onClick() {
      this.loading = true;

      setTimeout(() => {
        this.loading = false;
        this.loaded = true;
      }, 2000);
    },
  },
};
</script>

<style scoped>
.v-text-field {
  margin: 10px auto;
  max-width: 90vw;
}
</style>
