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
      <h2>{{ greetingMessage }}</h2>
    </div>
    
    <div class="main-content">
      <h2>به پنل ادمین خوش آمدید</h2>
    </div>
    <div class="chart-container">
      <h2>نمودار کاربران فعال</h2>
      <canvas ref="chartCanvas"></canvas>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { getFeatureConfig } from '../config/featureConfig'
import { getTokenPermissions } from '../auth'
import Chart from 'chart.js/auto'

const permissions = getTokenPermissions()
const { buttons } = getFeatureConfig(permissions)

const router = useRouter()
const sidebarOpen = ref(true)
const greetingMessage = ref('')
const chartCanvas = ref(null)

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

const mockChartData = () => {
  const hours = Array.from({ length: 24 }, (_, i) => i)
  const userCounts = hours.map(() => Math.floor(Math.random() * 100))
  const messageCounts = hours.map(() => Math.floor(Math.random() * 500))

  new Chart(chartCanvas.value.getContext('2d'), {
    type: 'line',
    data: {
      labels: hours.map(h => `${h}:00`),
      datasets: [
        {
          label: 'تعداد کاربران',
          data: userCounts,
          borderColor: '#4CAF50',
          backgroundColor: 'rgba(76, 175, 80, 0.1)',
          tension: 0.4,
          fill: true
        },
        {
          label: 'تعداد پیام‌ها',
          data: messageCounts,
          borderColor: '#2196F3',
          backgroundColor: 'rgba(33, 150, 243, 0.1)',
          tension: 0.4,
          fill: true
        }
      ]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            font: {
              family: 'IRANSans'
            }
          }
        },
        x: {
          ticks: {
            font: {
              family: 'IRANSans'
            }
          }
        }
      },
      plugins: {
        legend: {
          labels: {
            font: {
              family: 'IRANSans'
            }
          }
        }
      }
    }
  })
}

onMounted(() => {
  setGreetingMessage()
  mockChartData()
})

const toggleSidebar = () => {
  sidebarOpen.value = !sidebarOpen.value
}

const handleLogout = () => {
  localStorage.removeItem("access_token")
  localStorage.removeItem("token")
  window.location.href = "/login"
}

const handleDashboard = () => {
  router.push('/dashboard')
}

const navigate = async (route) => {
  const token = localStorage.getItem('token')
  try {
    await axios.get(`http://localhost:8082${route}`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    router.push(route)
  } catch (error) {
    if (error.response?.status === 403) {
      alert("شما دسترسی لازم را ندارید.")
    } else {
      alert(error.response?.status || "خطای نامشخص")
    }
  }
}
</script>


