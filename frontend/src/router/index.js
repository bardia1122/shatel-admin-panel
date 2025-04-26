import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import managedata from '../views/managedata.vue'
import accesskb from '../views/accesskb.vue'
import accessdb from '../views/accessdb.vue'
import viewlogs from '../views/viewlogs.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard },
  { path: '/access_db', component: accessdb },
  { path: '/manage_data', component: managedata },
  { path: '/logs', component: viewlogs },
  { path: '/access_kb', component: accesskb }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
router.beforeEach((to, from, next) => {
  const publicPages = ['/', '/login']
  const authRequired = !publicPages.includes(to.path)
  const token = localStorage.getItem('token')

  if (authRequired && !token) {
    return next('/') //if did not login
  }

  next()
})

export default router
