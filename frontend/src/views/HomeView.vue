<template>
  <div class="home">
    <h1>Image Classifier</h1>

    <input type="file" @change="onFileChange" />
    <button @click="uploadImage">Upload Image</button>

    <!-- Image display area -->
    <div v-if="uploadedImage">
      <h2>Uploaded Image:</h2>
      <img :src="uploadedImage" alt="Uploaded Image" style="max-width: 500px;"/>
    </div>

    <p v-if="prediction">The Prediction is: 
      <span v-if="prediction == 1"> Dog</span>
      <span v-if="prediction == 2"> Non-Dog</span>
    </p>

    <button @click="clearImage" v-if="uploadedImage">Clear Image</button>
  </div>
</template>


<script>
import axios from 'axios'

export default {
    data() {
        return {
            selectedFile: null,
            uploadedImage: null, // URL of the uploaded image
            prediction: null,
        };
    },
    methods: {
      onFileChange(e) {
        this.selectedFile = e.target.files[0];
        
        if (this.selectedFile) {
          this.uploadedImage = URL.createObjectURL(this.selectedFile);
        }
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

          this.prediction = response.data.prediction
          
          if(this.prediction == 0) {
            this.prediction = 2
          }
        } catch (error) {
          console.error('Upload error:', error);
        }
      },
      clearImage() {
        this.uploadedImage = null;
        this.selectedFile = null;
        this.prediction = null;
      },
    }
}
</script>

<style>
  .home {
    width: 80%;
    margin: 5rem auto;
  }
</style>
