<template>
  <!-- <div class="main">
    <div
      class="dropzone-container"
      @dragover="dragover"
      @dragleave="dragleave"
      @drop="drop"
    >
      <input
        type="file"
        name="file"
        id="fileInput"
        class="hidden-input"
        @change="onChange"
        ref="file"
        accept=".jpg,.jpeg,.png"
      />

      <label for="fileInput" class="file-label">
        <div v-if="isDragging">Release to drop files here.</div>
        <div v-else>Drop files here or <u>click here</u> to upload.</div>
      </label>
    </div>
  </div> -->
  <label class="label">
    <input type="file" class="input" name="" id="" />
    <span class="message"></span>
  </label>
</template>

<script>
export default {
  data() {
    return {
      isDragging: false,
      files: [],
    };
  },
  methods: {
    onChange(event) {
      this.files = [...this.$refs.file.files[0]];
      console.log(event);
    },
  },
};
</script>

<style scoped>
.label {
  /* @apply relative transition-all ease-in-out duration-300 */
  @apply relative transition-all ease-in-out duration-300 border border-gray-500 hover:bg-gray-400;
  /* position: relative;
  transition: all ease-in-out;
  transition-duration: 300ms;
  border: 2px white */
}

.input {
  /* @apply absolute top-0 left-0 w-full h-full hidden */
   @apply absolute top-0 left-0 w-full h-full hidden;
  /* visibility: hidden;
  position: absolute;
  top: 0px;
  left: 0px;
  width: 100%;
  height: 100%; */
}

.message {
  /* @apply absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 */
  @apply absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2; 
  /* position: absolute;
  top: 50%;
  left: 50%;
  transform: translateX(50%);
  transform: translateY(50%); */
}

.main {
  display: flex;
  flex-grow: 1;
  align-items: center;
  height: 80vh;
  justify-content: center;
  text-align: center;
}

.dropzone-container {
  /* padding: 4rem; */
  background: transparent;
}

.hidden-input {
  opacity: 0;
  /* overflow: hidden;
  position: absolute; */
  width: 1px;
  height: 1px;
}

.file-label {
  font-size: 20px;
  display: block;
  cursor: pointer;
  color: white;
}

.preview-container {
  display: flex;
  margin-top: 2rem;
}

.preview-card {
  display: flex;
  border: 1px solid #a2a2a2;
  padding: 5px;
  margin-left: 5px;
}

.preview-img {
  width: 50px;
  height: 50px;
  border-radius: 5px;
  border: 1px solid #a2a2a2;
  background-color: #a2a2a2;
}
</style>
