<template>
  <div class="container">
    <div class="row top">
      <h2>Список цветов</h2>
      <div class="label">
        <p class="col-12 pull-left color-string" v-for="color in getColors">
          <font-awesome-icon :icon="['fas', 'paw']" :style='{ color: color }' />
          {{ color }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: "Colors",
  data() {
    return {
    }
  },
  computed: {
    ...mapGetters(['getColors',])
  },
  methods: {
  },
}
</script>

<style>
.label {
  position: relative;
  width: 100%;
  height: 90%;
  overflow: auto;
}
.label::-webkit-scrollbar {
  width: 8px;
}
.label::-webkit-scrollbar-thumb {
  border-radius: 8px;
  background-color: white;
}
.color-string {
  font-size: 28px;
}
.top {
  height: 100%;
  padding: 0;
  width: inherit;
}
</style>
