import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Api from './views/Api.vue'
import Landing from './views/Landing.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'landing',
      component: Landing
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/api',
      name: 'api',
      component: Api
    }
  ]
})
