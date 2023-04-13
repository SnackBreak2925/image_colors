<template>
  <div class="main">
    <div
      class="label"
      v-bind="$attrs"
      @dragover="dragover"
      @dragleave="dragleave"
      @drop="drop"
    >
      <input
        type="file"
        name="file"
        id="fileInput"
        class="input"
        @change="onChange"
        ref="file"
        accept=".jpg,.jpeg,.png"
      />
      <span class="message" for="fileInput">
        <div v-if="isDragging">Release to drop files here.</div>
        <div v-else>Drop files here or <u>click here</u> to upload.</div>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isDragging: false,
      files: [],
      currentImage: undefined,
      previewImage: undefined,
      progress: 0,
      message: "",
      imageInfos: [],
    };
  },
  methods: {
    onChange(event) {
      this.files = [...this.$refs.file.files[0]];
      console.log(event);
    },
    dragover(e) {
      e.preventDefault();
      this.isDragging = true;
    },
    dragleave() {
      this.isDragging = false;
    },
    drop(e) {
      e.preventDefault();
      this.$refs.file.files = e.dataTransfer.files;
      this.onChange();
      this.isDragging = false;
    },
  },
};
</script>

<style scoped>
.main {
  display: flex;
  flex-grow: 1;
  align-items: center;
  height: 100vh;
  justify-content: center;
  text-align: center;
}

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
  background: transparent;
}

.hidden-input {
  opacity: 0;
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
