<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: 'vue-tray'
  }
</script>
import bus from '@/bus'
  mounted () {
    bus.$on('ping', () => {
      // event logic
      console.log('pong')
    })
  }
<style>
  /* CSS */
</style>
