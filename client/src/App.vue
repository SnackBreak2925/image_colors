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
  text-align: center;
  max-width: 100vw;
  width: 100%;
  height: 100vh;
  color: white;
  font-family: "fewriter";
}
</style>
