<template>
  <v-container grid-list-md text-xs-center class="books">
    <v-layout row wrap>
      <v-flex sm8 offset-sm2>
        <v-chip color="primary" text-color="white">
          <v-avatar class="teal">C</v-avatar>
          Books
        </v-chip>
        <!-- <v-card> -->

          <v-toolbar color="cyan" dark relative scroll-target="#scrolling-techniques">
            <v-toolbar-title>Books ({{books.length}} are shown)</v-toolbar-title>
            <v-spacer></v-spacer>

            <v-btn icon @click.native="setBooks">
              <v-icon>add_circle</v-icon>
            </v-btn>

            <v-btn icon @click.native="clearBooks">
              <v-icon>remove_circle</v-icon>
            </v-btn>
          </v-toolbar>
          <v-divider></v-divider>

          <div id="scrolling-techniques" class="scroll-y" style="max-height: 400px;">
            <v-list two-line>
              <template v-for="(book, index) in books">
                <v-divider :key="index"></v-divider>
                <v-list-tile :key="book.index">
                  <v-list-tile-content>
                    <v-list-tile-title v-html="book.title"></v-list-tile-title>
                    <v-list-tile-sub-title v-html="book.author"></v-list-tile-sub-title>
                  </v-list-tile-content>
                </v-list-tile>
              </template>
            </v-list>
          </div>

          <p>{{error}}</p>
        <!-- </v-card> -->
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import {
  mapState,
  mapActions
} from 'vuex'

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
