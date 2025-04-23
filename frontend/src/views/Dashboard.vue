<template>
  <div class="dashboard-container">
    <!-- Sidebar -->
    <div :class="['sidebar', { collapsed: !sidebarOpen }]">
      <div class="sidebar-toggle" @click="toggleSidebar">☰</div>

      <transition name="fade-slide">
        <div v-if="sidebarOpen" class="button-list">
          <button :class="{'active': true}" @click="handleDashboard">داشبورد</button>
          <button
            v-for="btn in buttons"
            :key="btn.key"
            @click="navigate(btn.route)"
          >
            {{ btn.label }}
          </button>
          <button class="logout-btn" @click="handleLogout">خروج</button>
        </div>
      </transition>
    </div>

    <div class="main-content">
      <h1>{{ greetingMessage }}</h1>
    </div>
    
    <div class="main-content">
      <h2>به پنل ادمین خوش آمدید</h2>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import axios from 'axios'
import { getFeatureConfig } from '../config/featureConfig'
import { getTokenPermissions } from '../auth'

const permissions = getTokenPermissions()
const { buttons } = getFeatureConfig(permissions)

const router = useRouter()
const sidebarOpen = ref(true)


const greetingMessage = ref('')

const setGreetingMessage = () => {
  const hours = new Date().getHours()

  if (hours >= 5 && hours < 12) {
    greetingMessage.value = 'سلام! صبح بخیر'
  } else if (hours >= 12 && hours < 17) {
    greetingMessage.value = 'سلام! ظهر بخیر'
  } else if (hours >= 17 && hours < 20) {
    greetingMessage.value = 'سلام! عصر بخیر'
  } else {
    greetingMessage.value = 'سلام! شب بخیر'
  }
}

setGreetingMessage()

const handleLogout = () => {
  localStorage.removeItem("access_token")
  localStorage.removeItem("token")
  window.location.href = "/login"
}

const toggleSidebar = () => {
  sidebarOpen.value = !sidebarOpen.value
}

const handleDashboard = () => {
  router.push('/dashboard')
}

const navigate = async (route) => {
  const token = localStorage.getItem('token')
  console.log("Token being sent:", token)

  try {
    const response = await axios.get(`http://localhost:8000${route}`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    router.push(route)
  } catch (error) {
    if (error.response && error.response.status === 403) {
      alert("شما دسترسی لازم را ندارید.")
    } else {
      alert(error.response.status)
    }
  }
}
</script>

