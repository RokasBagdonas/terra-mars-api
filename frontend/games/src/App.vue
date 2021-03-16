<template>
  <div>
    <button
      class="btn btn-primary btn-margin"
      v-if="!authenticated"
      @click="login()"
    >
      Log In
    </button>

    <button
      class="btn btn-primary btn-margin"
      v-if="authenticated"
      @click="privateMessage()"
    >
      Call Private
    </button>
    <button
      class="btn btn-primary btn-margin"
      v-if="authenticated"
      @click="logout()"
    >
      Log Out
    </button>
    {{ message }}
    <br />
  </div>

  <NavBar v-if="auth.authenticated"/>
  <router-view v-if="auth.authenticated"/>

</template>


<script lang="ts">
import Vue from "vue";
import NavBar from "./components/NavBar.vue";
// Auth
import AuthService from "./auth/AuthService";
import axios from "axios";

const API_URL = "http://localhost:8000";
const auth = new AuthService();
// ------

export default {
  components: {
    NavBar,
  },
  setup(){
    let auth = new AuthService();
    auth.handleAuthentication();
    auth.authenticated = false;
    auth.authNotifier.on("authChange", (authState) => {
      auth.authenticated = authState.authenticated;
    });

    return {
      auth,
      message: "",
    };

  },
};
</script>
