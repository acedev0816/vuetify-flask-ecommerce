<template>
  <div class="about">
    <h1>Backend Resources Demo</h1>
    <Books/>
    <keep-alive>
      <VegaCars/>
    </keep-alive>
  </div>
</template>

<script>
import Books from '@/components/Books'
import VegaCars from '@/components/VegaCars'

export default {
  components: {
    Books,
    VegaCars
  }
}

</script>

<style lang="scss">
</style>
