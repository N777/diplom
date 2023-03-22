<template>
  <v-row no-gutters justify="center">
    <v-dialog v-model="dialog" width="1024">
      <template v-slot:activator="{ props }">
        <div v-if="isAuth" class="d-flex justify-space-between align-center">
          <v-chip>{{ userInfo?.email }}</v-chip>
          <v-btn v-on:click="deleteToken">Logout</v-btn>
        </div>
        <v-btn v-else color="primary" v-bind="props"> Login</v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">User Profile</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="Email*"
                  required
                  v-model="email"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  label="Password*"
                  type="password"
                  v-model="password"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue-darken-1" variant="text" @click="submitLoginForm">
            LogIn
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import axios from "axios";
import { mapActions, mapState } from "vuex";

export default {
  data: () => ({ dialog: false, email: "", password: "" }),
  props: {
    openDialog: Boolean,
  },
  computed: {
    ...mapState(["isAuth", "userInfo"]),
  },
  methods: {
    ...mapActions(["addToken", "deleteToken"]),
    submitLoginForm() {
      const formData = {
        email: this.email,
        password: this.password,
      };
      axios.post("auth/token/login", formData).then((response) => {
        this.addToken(response.data.auth_token);
        this.dialog = false;
      });
    },
  },
  // computed: {
  //   // геттер вычисляемого значения
  //   dialog: function () {
  //     // `this` указывает на экземпляр vm
  //     return this.openDialog;
  //   },
  // },
  name: "VLoginModel",
};
</script>

<style scoped></style>
