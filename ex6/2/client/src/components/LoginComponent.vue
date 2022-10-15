<template>
  <div id="loginContainer">
    <div id="loginTitle">
      <label>Please login!</label>
    </div>

    <div id="username">
      <label id="usernameLabel">Username:</label>
      <input data-testid="usernameTextArea" v-model="username" />
    </div>

    <div id="password">
      <label id="passwordLabel">Password: </label>
      <input
        type="password"
        data-testid="passwordTextArea"
        v-model="password"
      />
    </div>

    <div id="loginButton">
      <button v-on:click="handleClickSignin">Sign in</button>
    </div>

    <div id="loginDisplay">
      <label id="loginStatusLabel">{{ loginStatus }}</label>
    </div>
  </div>
</template>

<script>
import { doLogin } from "@/utils/apiutils.js";

const CryptoJS = require("crypto-js");
const SALT_CONST = "supersecretsalt"; //Unsecure salt, only used to save time on this exercise
const KEY_SIZE = 32;
const ITERATIONS = 2048;

const hashPassword = (pass) =>
  CryptoJS.PBKDF2(pass, SALT_CONST, {
    keySize: KEY_SIZE,
    iterations: ITERATIONS,
  }).toString();

export default {
  name: "LoginComponent",
  data: function () {
    return {
      username: "",
      password: "",
      loginStatus: "",
    };
  },
  methods: {
    async handleClickSignin() {
      const loginRequest = {
        userName: this.username,
        password: hashPassword(this.password),
      };

      const loginResponse = doLogin(loginRequest);
      loginResponse.then((result) => {
        this.loginStatus = result;
        alert(result);
      });
    },
  },
};
</script>

<style scoped>
#loginContainer {
  display: grid;
  justify-content: center;
  text-align: center;
  margin: 40px;
}

#loginTitle {
  font-size: x-large;
  font-weight: bold;
  margin-bottom: 20px;
}

#username,
#password {
  padding-top: 10px;
  display: flex;
  flex-direction: row;
  align-items: center;
  column-gap: 10px;
}

#loginButton {
  padding-top: 30px;
}

#usernameLabel,
#passwordLabel {
  width: 100px;
}

#loginDisplay {
  padding-top: 10px;
}
</style>
