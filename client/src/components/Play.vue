<template>
  <div class="container">
    <img class="play-button" src="../assets/play_button.svg" @click="play" />
  </div>
</template>

<script>
export default {
  name: "Play",
  data() {
    return {
      counter: 0,
    };
  },
  methods: {
    play() {
      console.log(this.counter);
      this.counter++;
    },
  },
};
</script>

<style>
.container {
  display: flex;
  align-items: center;
  position: relative;
  flex-grow: 1;
  height: 80vh;
  justify-content: center;
  text-align: center;
}

.play-button {
  max-width: 30%;
}
</style>
