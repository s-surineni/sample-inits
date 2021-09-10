<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import bus from '@/bus'

export default {
  name: 'vue-tray',

  mounted () {
    bus.$on('ping', () => {
      // event logic
      console.log('pong')
    })
  }
}
</script>

<style>
/* CSS */
</style>
