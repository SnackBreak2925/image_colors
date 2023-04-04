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
    <span class="message">Drop or click to upload image</span>
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
  height: 60vh;
  position: relative;
  width: 100%;
  height: 100%;
  cursor: pointer;
}

.input {
  visibility: hidden;
  position: absolute;
  top: 0px;
  left: 0px;
  width: 100%;
  height: 100%;
}

.message {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
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
