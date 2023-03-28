<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
@font-face {
  font-family: "fewriter";
  src: url("~@/assets/fonts/fewriter.ttf");
}
#app {
  margin: 0;
  background-image: url("~@/assets/background.png");
  background-repeat: repeat;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  width: 100%;
  height: 100vmin;
}
</style>
