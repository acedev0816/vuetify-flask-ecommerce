<template>
  <v-container class="books">
    <v-layout>
      <v-flex>

        <v-chip color="primary" text-color="white">
          <v-avatar class="teal">C</v-avatar>
          Books
        </v-chip><br>
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
