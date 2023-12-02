<template>
  <div class="home">
    <h1>Homepage</h1>

    <button @click="test">Click me</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {

        };
    },
    methods: {
      async test() {
        try {
            const response = await axios.get('http://127.0.0.1:8000/test/');

            console.log(response.data.message)
        } catch (error) {
          console.log(error)
        }

        this.userInput = ''
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