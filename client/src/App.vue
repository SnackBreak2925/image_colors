<template>
  <b-overlay bg-color="transparent" spinner-variant="white" blur="20px" :show="isLoading" rounded="sm">
    <div id="app">
        <router-view />
    </div>
  </b-overlay>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "App",
  computed: {
    ...mapGetters(["isLoading"]),
  },
};
</script>

<style>
@font-face {
  font-family: "fewriter";
  src: url("~@/assets/fonts/fewriter.ttf");
}
#app {
  margin: 0;
  text-align: center;
  max-width: 100vw;
  width: 100%;
  height: 100vh;
  color: white;
  font-family: "fewriter";
}
</style>
