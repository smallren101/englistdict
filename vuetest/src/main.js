import Vue from 'vue'
import './plugins/axios'
import ElementUI from "element-ui"
import "element-ui/lib/theme-chalk/index.css"
import App from './App.vue'
import './plugins/element.js'
import router from './router'
import axios from "axios"

import service from './request'

Vue.config.productionTip = false

Vue.prototype.$request = service;
// axios.defaults.headers.post['Content-Type'] = 'application/json';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
axios.defaults.withCredentials = true;
Vue.prototype.$ajax = axios;

Vue.use(ElementUI)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
