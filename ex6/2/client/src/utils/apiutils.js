import axios from "axios";

export function doLogin(loginRequest) {
  return axios
    .post(`http://localhost:8080/login`, loginRequest, {
      auth: {
        username: loginRequest.username,
        password: loginRequest.password,
      },
    })
    .then((response) => {
      return response.data;
    });
}
