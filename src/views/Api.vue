<template>
  <div class="about">
    <h1>Backend Resources Demo</h1>
    <p>Click on the links below to fetch data from the Flask server</p>
    <!-- <a href="" @click.prevent="fetchResource">Fetch</a><br/>
    <a href="" @click.prevent="fetchSecureResource">Fetch Secure Resource</a><br> -->
    <a href="" @click.prevent="fetchBooks">books</a>
    <h4>Results</h4>
    <!-- <p v-for="r in resources" :key="r.timestamp">
      Server Timestamp: {{r.timestamp | formatTimestamp }}
    </p> -->
    <ul>
      <li v-for="book in books" v-bind:key="book.id">{{book.title}}</li>
    </ul>
    <p>{{error}}</p>
  </div>
</template>

<script>

import $backend from '../backend'

export default {
  name: 'about',
  data () {
    return {
      resources: [],
      error: '',
      books: null
    }
  },
  methods: {
    fetchResource () {
      $backend.fetchResource()
        .then(responseData => {
          this.resources.push(responseData)
        }).catch(error => {
          this.error = error.message
        })
    },
    fetchSecureResource () {
      $backend.fetchSecureResource()
        .then(responseData => {
          this.resources.push(responseData)
        }).catch(error => {
          this.error = error.message
        })
    },
    fetchBooks () {
      $backend.fetchBooks()
        .then(response => {
          console.log(response.data)
          this.books = response.data
        }).catch(error => {
          this.error = error.message
        })
    }
  }
}

</script>

<style lang="scss">
</style>
