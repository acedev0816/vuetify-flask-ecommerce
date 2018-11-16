<template>
  <v-container class="books">
    <v-layout>
      <v-flex>
        <p>Click on the links below to fetch data from the Flask server</p>
        <!-- <a href="" @click.prevent="fetchResource">Fetch</a><br/>
      <a href="" @click.prevent="fetchSecureResource">Fetch Secure Resource</a><br> -->
        <v-btn @click.native="setBooks">fetch books</v-btn>
        <v-btn @click.native="clearBooks">clear books</v-btn>
        <!-- <a href="" @click.prevent="setBooks">fetch books</a> -->
        <h4>Results</h4>

        <ul>
          <li v-for="book in books" v-bind:key="book.id">{{book.title}}</li>
        </ul>
        <p>{{error}}</p>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'books',
  methods: {
    ...mapActions(['setBooks', 'clearBooks'])
    // fetchResource () {
    //   $backend.fetchResource()
    //     .then(responseData => {
    //       this.resources.push(responseData)
    //     }).catch(error => {
    //       this.error = error.message
    //     })
    // },
    // fetchSecureResource () {
    //   $backend.fetchSecureResource()
    //     .then(responseData => {
    //       this.resources.push(responseData)
    //     }).catch(error => {
    //       this.error = error.message
    //     })
    // },
  },
  computed: {
    ...mapState(['books', 'error'])
  }
}
</script>
