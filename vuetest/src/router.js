import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import IndexPage from "./views/IndexPage.vue"

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  // base: 'http://127.0.0.1:5000/api1',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: {
        
      },
      children: [{
        path: "/danci",
        name: "danci",
        component: IndexPage,
        meta: {
          keepAlive: false,
        }
      }]
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
