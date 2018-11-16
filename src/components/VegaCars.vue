<template>
  <v-container class="vega_cars">
    <v-layout>
      <v-flex>
        <v-chip color="primary" text-color="white">
          <v-avatar class="teal">C</v-avatar>
          VegaCars
        </v-chip><br>
        <v-card>

          <div id="vega-display"></div>
          <v-btn @click="setCars">fetch cars</v-btn>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import vegaEmbed from 'vega-embed'

export default {
  name: 'vega_cars',
  data () {
    return {
      spec: null
    }
  },
  methods: {
    ...mapActions(['setCars'])
  },
  computed: {
    ...mapState(['cars'])
  },
  watch: {
    cars: (cars) => {
      console.log('$store.state.cars changed value')
      if (cars) {
        vegaEmbed('#vega-display', cars, {actions: false})
      }
    }
  }
}
</script>
