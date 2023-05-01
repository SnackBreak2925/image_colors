<template>
  <div class="container">
    <div v-if="files.length > 1" class="top">
      <p>Загрузке подлежит только <b>один</b> файл</p>
      <button class="remove" type="button" @click="removeAll" title="Удалить все">
        <b>Удалить все</b>
      </button>
    </div>
    <div v-else-if="files.length && checkFilesType()" class="top">
      <p>Загрузке подлежат только <b>изображения</b></p>
      <button class="remove" type="button" @click="removeAll" title="Удалить все">
        <b>Удалить все</b>
      </button>
    </div>
    <div
      v-else-if="!files.length"
      class="label"
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
      <label class="message" for="fileInput">
        <div v-if="isDragging">Отпустите кнопку мыщи чтобы загрузить файл.</div>
        <div v-else>Перетащите или <u>нажмите сюда</u> чтобы загрузить файлы.</div>
      </label>
    </div>
    <div v-else class="preview-container">
      <img :key="files[0].name" class="preview-img" :src="generateURL(files[0])" />
      <button class="remove" type="button" @click="removeAll" title="Удалить изображение">
        <b>Удалить</b>
      </button>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "Upload",
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
  computed: {},
  methods: {
    ...mapActions(["storeFile", "deleteFiles"]),
    onChange() {
      this.files = [...this.$refs.file.files];
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
    checkFilesType() {
      if (/image/.test(this.files[0]["type"])) return false;
      else return true;
    },
    removeAll(i) {
      this.files = [];
      this.deleteFiles();
    },
    generateURL(file) {
      this.storeFile(file);
      let fileSrc = URL.createObjectURL(file);
      setTimeout(() => {
        URL.revokeObjectURL(fileSrc);
      }, 1000);
      return fileSrc;
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
  cursor: pointer;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.preview-container {
  flex-direction: column;
  height: 100%;
}

.preview-img {
  object-fit: contain;
  height: 95%;
  width: 100%;
  background-color: rgba(0, 0, 0, 0);
}

.top {
  display: flex;
  flex-direction: column;
}

.remove {
  position: sticky;
  top: 100%;
  border: 2px solid white;
  color: white;
  background-color: rgba(0, 0, 0, 0);
}
</style>
