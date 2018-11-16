<template>
  <div class="home">
    <VueInfo msg="Welcome to the Vue.js + Vuetify + Flask + Vega App Example"/>
  </div>
</template>

<script>
// @ is an alias to /src
import VueInfo from '@/components/VueInfo.vue'

export default {
  name: 'home',
  components: {
    VueInfo
  }
}
</script>

<style lang="scss">

</style>
