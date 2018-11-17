<template>
  <v-container grid-list-md text-xs-center class="books">
    <v-layout row wrap>
      <v-flex sm8 offset-sm2>
        <v-chip color="primary" text-color="white">
          <v-avatar class="teal">C</v-avatar>
          VegaCars
        </v-chip><br>

        <v-toolbar color="cyan" dark relative scroll-target="#scrolling-techniques">
          <v-toolbar-title>Cars</v-toolbar-title>
          <v-spacer></v-spacer>

          <v-btn icon @click.native="setCars">
            <v-icon>add_circle</v-icon>
          </v-btn>

          <v-btn icon @click.native="clearCars">
            <v-icon>remove_circle</v-icon>
          </v-btn>
        </v-toolbar>
        <v-divider></v-divider>

        <div v-show="cars" id="vega-display"></div>

      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import {
  mapState,
  mapActions
} from 'vuex'
import vegaEmbed from 'vega-embed'

export default {
  name: 'vega_cars',
  methods: {
    ...mapActions(['setCars', 'clearCars'])
  },
  computed: {
    ...mapState(['cars'])
  },
  watch: {
    cars: (spec) => {
      console.log('$store.state.cars changed value')
      if (spec) {
        vegaEmbed('#vega-display', spec, {
          actions: false
        })
      }
    }
  }
}
</script>
