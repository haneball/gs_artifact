import Vue from 'vue'
import Router from 'vue-router'
import MyApp from '../components/MyApp'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'MyApp',
      component: MyApp,
      meta: {
        title: 'gs_artifact'
      }
    }
  ]
})
