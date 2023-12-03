<template>
  <div class="home">
    <h1>Homepage</h1>

    <input type="file" @change="onFileChange" />
    <button @click="uploadImage">Upload Image</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            selectedFile: null,
        };
    },
    methods: {
      onFileChange(e) {
        this.selectedFile = e.target.files[0];
      },
      async uploadImage() {
        if (!this.selectedFile) {
          alert('Please select an image first!');
          return;
        }

        const formData = new FormData();
        formData.append('image', this.selectedFile);

        try {
          const response = await axios.post('http://127.0.0.1:8000/upload/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });

          console.log('Image uploaded:', response.data);
        } catch (error) {
          console.error('Upload error:', error);
        }
      }
    }
}
</script>

<style>
  .home {
    width: 80%;
    margin: 5rem auto;
  }
</style>
