<template>
  <!-- v-if="!(this.$store.state.loginStatus == 'Success')" -->
  <div id="loginContainer">
    <div id="loginTitle">
      <label>Please login!</label>
    </div>

    <div id="username">
      <label id="usernameLabel">Username:</label>
      <input data-testid="usernameTextArea" v-model="username" />
      <!-- <textarea data-testid="usernameTextArea" v-model="username"></textarea> -->
    </div>

    <div id="password">
      <label id="passwordLabel">Password: </label>
      <input
        type="password"
        data-testid="passwordTextArea"
        v-model="password"
      />
      <!-- <textarea type="password" data-testid="passwordTextArea" v-model="password"></textarea> -->

      <button v-on:click="handleClickSignin">Sign in</button>
      <label id="loginstatusLabel">{{ loginStatus }}</label>
    </div>
  </div>
</template>

<script>
// import { doLogin } from '@/utils/apiutils.js'

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
      console.log("Ye");
      // const loginRequest = {
      //     username: this.username,
      //     password: this.password
      // };
      // await this.$store.dispatch('setUsername', this.username)
      // await this.$store.dispatch('setPassword', this.password)

      // const loginResponse = doLogin(loginRequest);
      // loginResponse.then((resolvedResult) => {
      //     this.loginStatus = resolvedResult.loginStatus;
      //     alert("Login: " + resolvedResult.loginStatus);
      //     this.$store.dispatch('setLoginStatus', this.loginStatus);
      // });
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

#usernameLabel,
#passwordLabel {
  width: 100px;
}

#loggedInView {
  text-align: center;
  margin-top: 30px;
}
</style>
