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
.play-button {
  max-width: 30%;
}
</style>
