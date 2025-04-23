<template>
    <div class="dashboard-container">
      <!-- Sidebar -->
      <div :class="['sidebar', { collapsed: !sidebarOpen }]">
        <div class="sidebar-toggle" @click="toggleSidebar">☰</div>
        <transition name="fade-slide">
          <div v-if="sidebarOpen" class="button-list">
            <button @click="handleDashboard">داشبورد</button>
            <button
              v-for="btn in buttons"
              :key="btn.key"
              :class="{ active: btn.route === currentRoute }"
              @click="navigate(btn.route)"
            >
              {{ btn.label }}
            </button>
            <button class="logout-btn" @click="handleLogout">خروج</button>
          </div>
        </transition>
      </div>
  
      <!-- Main Content -->
      <div class="main-content">
        <div class="export-card">
          <h2>دسترسی به پایگاه داده</h2>
          <p>برای بروزرسانی دیتابیس روی دکمه زیر کلیک کنید</p>
          <button @click="updateDatabase" class="export-button">
            بروزرسانی دیتابیس
          </button>
  
          <div v-if="message" :class="['message', messageType]" style="margin-top: 1.5rem;">
            {{ message }}
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { getFeatureConfig } from '../config/featureConfig'
  import { getTokenPermissions } from '../auth'
  import { useRouter, useRoute } from 'vue-router'
  import axios from 'axios'
  
  const sidebarOpen = ref(true)
  const message = ref('')
  const messageType = ref('success')
  const router = useRouter()
  const route = useRoute()
  const currentRoute = route.path
  const permissions = getTokenPermissions()
  const { buttons } = getFeatureConfig(permissions)
  
  const updateDatabase = async () => {
    try {
      const response = await axios.post('http://localhost:8000/update-database', {}, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
      })
      message.value = 'دیتابیس با موفقیت بروزرسانی شد'
      messageType.value = 'success'
    } catch (error) {
      message.value = 'خطا در بروزرسانی دیتابیس'
      messageType.value = 'error'
      console.error('Error:', error)
    }
  }
  
  const toggleSidebar = () => {
    sidebarOpen.value = !sidebarOpen.value
  }
  
  const handleLogout = () => {
    localStorage.removeItem("access_token")
    localStorage.removeItem("token")
    window.location.href = "/login"
  }
  
  const navigate = async (route) => {
    const token = localStorage.getItem('token')
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
  
  const handleDashboard = () => {
    router.push("/dashboard")
  }
  </script>
