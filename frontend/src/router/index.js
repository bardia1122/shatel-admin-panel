import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import managedata from '../views/managedata.vue'
import accesskb from '../views/accesskb.vue'
import accessdb from '../views/accessdb.vue'

import RedirectLogs from '../views/RedirectLogs.vue'

const routes = [
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard },
  { path: '/access_db', component: accessdb },
  { path: '/manage_data', component: managedata },
  { path: '/logs', component: RedirectLogs },
  { path: '/access_kb', component: accesskb }
]


const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['/login'];
  const authRequired = !publicPages.includes(to.path);
  const token = localStorage.getItem('token');
  console.log(token)
  if (to.path === '/') {
    // User opened root "/"
    if (token) {
      return next('/dashboard'); // token exists -> go to dashboard
    } else {
      return next('/login'); // no token -> go to login
    }
  }

  if (authRequired && !token) {
    return next('/login'); // if trying to access protected page without token
  }

  next(); // otherwise allow
});


export default router
