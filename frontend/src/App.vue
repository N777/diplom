<script>
export default {
  data() {
    return {
      users: [
        { name: "qwe", age: 12 },
        { name: "qw8", age: 15 },
        { name: "qw7", age: 19 },
      ],
    };
  },
  methods: {
    addUser() {
      this.users.push({
        name: "Rtrd",
        age: 15,
      });
    },
  },
};
</script>

<template>
  <main>
    <div>
      <button @click="addUser"></button>
      <ul>
        <li v-for="user in users" :key="user.name">
          {{ user.name }}
          {{ user.age }}
        </li>
      </ul>
    </div>
  </main>
</template>
