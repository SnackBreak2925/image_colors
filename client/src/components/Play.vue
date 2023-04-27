<template>
  <div class="container">
    <img class="play-button" src="../assets/play_button.svg" @click="play" />
  </div>
</template>

<script>
import { mapMutations, mapActions, mapGetters } from 'vuex'
export default {
  name: "Play",
  data() {
    return {
      counter: 0,
    };
  },
  computed: {
    ...mapGetters({mainCount: 'counts'}),
  },
  methods: {
    play() {
      // console.log(this.counter);
      // this.counter++;
      console.log(this.mainCount)
    },
  },
};
</script>

<style>
.play-button {
  max-width: 30%;
}
</style>
