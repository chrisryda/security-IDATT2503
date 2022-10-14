import { createStore } from "vuex";

export default createStore({
  state: {
    username: '',
    password: '',
    loginStatus: ''
  },
  mutations: {
    SET_USERNAME(state, username) {
      state.username = username
    },
    SET_PASSWORD(state, password) {
      state.password = password
    },
    SET_LOGIN_STATUS(state, status) {
      state.loginStatus = status
    }
  },
  actions: {
    setUsername(context, username) {
      context.commit('SET_USERNAME', username)
    },
    setPassword(context, password) {
      context.commit('SET_PASSWORD', password)
    },
    setLoginStatus(context, status) {
      context.commit('SET_LOGIN_STATUS', status)
    }
  }
});
