<template>
  <div>
    <appheader />
    <div class="row container-fluid">
      <div class="col-6">
        <upload />
      </div>
      <div class="col-6">
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
.container {
  margin-top: 30px;
  overflow: auto;
}
</style>
