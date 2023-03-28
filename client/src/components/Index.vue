<template>
  <div>
    <appheader />
    <div class="row container-fluid">
      <div class="col-4 upload">
        <upload />
      </div>
      <div class="col-4">
        <p>text</p>
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

export default {
  name: "Index",
  components: {
    appheader: Header,
    upload: Upload,
    colorList: Colors,
  },
};
</script>

<style>
.container-fluid {
  margin-top: 30px;
  overflow: auto;
}
.upload {
  border: 2px solid white;
}
.color-list {
  border: 2px solid white;
}
</style>
