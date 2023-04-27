<template>
  <div class="container play-element">
    <transition name="fade">
      <img
        v-if="typeof wannaColors == 'number'"
        class="play-button"
        src="../assets/play_button.svg"
        @click="play"
      />
    </transition>
    <div class="selecting">
      <p>Количество цветов</p>
      <!-- TODO change input of coloors -->
      <select v-model="wannaColors">
        <option :value="null"></option>
        <option v-for="index in 15" :value="index">
          {{ index }}
        </option>
      </select>
    </div>
  </div>
</template>

<script>
import { mapMutations, mapActions, mapGetters } from "vuex";
export default {
  name: "Play",
  data() {
    return {
      counter: 0,
      wannaColors: null,
    };
  },
  computed: {
    ...mapGetters({ mainCount: "counts" }),
  },
  methods: {
    play() {
      console.log(this.mainCount);
    },
  },
};
</script>

<style>
.play-button {
  max-width: 30%;
}

.play-element {
  flex-direction: column;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.selecting {
  width: 50%;
  position: absolute;
  bottom: 20%;
}

.select-list {
  overflow: auto;
  height: 20%;
}
</style>
