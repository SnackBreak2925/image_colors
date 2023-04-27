<template>
  <div class="container">
    <div class="row top">
      <h2>Список цветов</h2>
      <div class="label">
        <p class="col-12 pull-left color-string" v-for="color in colors">
          <font-awesome-icon :icon="['fas', 'paw']" :style='{ color: color }' />
          {{ color }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Colors",
  data() {
    return {
      colors: [
        '#567b89',
        '#ffbaed',
        '#a84532',
        '#567b89',
        '#67487d',
        '#e0d6ff',
        '#bad6f0',
        '#567b89',
        '#ffbaed',
        '#a84532',
        '#567b89',
        '#67487d',
        '#e0d6ff',
        '#bad6f0',
        '#bad6f0',
      ]
    }
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
