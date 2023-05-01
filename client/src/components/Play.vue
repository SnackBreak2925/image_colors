<template>
  <div class="container play-element">
    <transition name="fade">
      <img
        v-if="typeof wannaColors == 'number' && getFile"
        class="play-button"
        src="../assets/play_button.svg"
        @click="sendFile"
      />
    </transition>
    <div class="selecting">
      <p>Количество цветов</p>
      <b-form-select
        size="sm"
        class="dropdown-list"
        v-model="wannaColors"
        :options="dropOptions"
        @change="setCountColors(wannaColors)"
      />
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Play",
  data() {
    return {
      counter: 0,
      wannaColors: null,
      dropOptions: [],
    };
  },
  computed: {
    ...mapGetters(['getFile']),
  },
  methods: {
    ...mapActions(['sendFile', 'setCountColors',]),
    setOptions() {
      this.dropOptions.push({ value: null, text: "Выбрать" });
      for (let i = 1; i <= 15; i++) {
        this.dropOptions.push({ value: i, text: i });
      }
    },
  },
  beforeMount() {
    this.setOptions();
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
  top: 0;
}

.dropdown-list {
  background: inherit;
  color: inherit;
  border: 2px solid white;
}

option {
  color: white;
  background: black;
}
</style>
