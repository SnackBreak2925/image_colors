<template>
  <div>
    <appheader />
    <div class="row">
      <div class="col-4 bordered">
        <upload />
      </div>
      <div class="col-4">
        <play />
      </div>
      <div class="col-4 bordered color-list">
        <colorList />
      </div>
    </div>
  </div>
</template>

<script>
import upload from "./Upload.vue";
import appheader from "./Header.vue";
import colorList from "./Colors.vue";
import play from "./Play.vue";

export default {
  name: "Index",
  components: {
    appheader,
    upload,
    colorList,
    play,
  },
};
</script>

<style>
.container {
  display: flex;
  align-items: center;
  position: relative;
  flex-grow: 1;
  height: 100%;
  justify-content: center;
  text-align: center;
  padding: 0;
}
.bordered {
  height: 80vh;
  border: 2px solid white;
}
.row {
  margin: 0;
  padding-left: 2vw;
  padding-right: 2vw;
}
.color-list {
  padding-top: 15px;
}
</style>
