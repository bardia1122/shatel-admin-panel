import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'

const AccessDB = { template: '<h2>دسترسی به پایگاه</h2>' }
const ManageData = { template: '<h2>مدیریت داده</h2>' }
const Logs = { template: '<h2>گزارش و تاریخچه</h2>' }
const AccessKB = { template: '<h2>دسترسی به پایگاه دانش</h2>' }

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard },
  { path: '/access-db', component: AccessDB },
  { path: '/manage-data', component: ManageData },
  { path: '/logs', component: Logs },
  { path: '/access-kb', component: AccessKB }
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
