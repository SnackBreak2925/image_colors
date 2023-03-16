<template>
  <div>
    <header>
      <appheader />
    </header>
    <div class="container">
      <upload />
    </div>
  </div>
</template>

<script>
import Upload from './Upload.vue';
import Header from './Header.vue';

export default {
  name: 'Index',
  components: {
    appheader: Header,
    upload: Upload,
  },
};
</script>

<style>
.container {
  margin-top: 30px;
  overflow: auto;
}
</style>
