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
      <b-dropdown class="select-list" v-model="wannaColors">
        <b-dropdown-item-button :value="null"></b-dropdown-item-button>
        <b-dropdown-item-button v-for="index in 15" :value="index">
          {{ index }}
        </b-dropdown-item-button>
      </b-dropdown>
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

::v-deep .select-list {
  overflow: auto;
  height: 15%;
}
</style>
