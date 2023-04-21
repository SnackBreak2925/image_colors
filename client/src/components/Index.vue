<template>
  <div>
    <appheader />
    <div class="row">
      <div class="col-4 upload">
        <upload />
      </div>
      <div class="col-4">
        <play />
      </div>
      <div class="col-4 color-list">
        <colorList />
      </div>
    </div>
  </div>
</template>

<script>
import Upload from "./Upload.vue";
import Header from "./Header.vue";
import Colors from "./Colors.vue";
import Play from "./Play.vue";

export default {
  name: "Index",
  components: {
    appheader: Header,
    upload: Upload,
    colorList: Colors,
    play: Play,
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

.upload {
  border: 2px solid white;
  padding: 0;
}
.color-list {
  border: 2px solid white;
  padding: 0;
}
.row {
  margin-top: 30px;
  height: 75vh;
  margin-left: 0;
  margin-right: 0;
  padding-left: 2vw;
  padding-right: 2vw;
}
</style>
