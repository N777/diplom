<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent width="1024">
      <template v-slot:activator="{ props }">
        <v-btn color="primary" v-bind="props"> Login </v-btn>
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

export default {
  data: () => ({ dialog: false, email: "", password: "" }),
  props: {
    openDialog: Boolean,
  },
  methods: {
    submitLoginForm() {
      const formData = {
        login: this.email,
        password: this.password,
      };
      axios.post("auth/token/login", formData).then((response) => {
        console.log(response.data);
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
