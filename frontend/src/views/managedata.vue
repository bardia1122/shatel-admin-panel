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
        <h2>صدور داده‌های چت</h2>
        <!-- Start Date -->
        <div class="input-group">
          <label class="block mb-2 text-lg font-medium">تاریخ شروع</label>
          <input
            v-model="startDate"
            type="date"
            class="border border-gray-600 rounded-xl px-4 py-3 w-full focus:ring-2 focus:ring-orange-500 focus:outline-none transition duration-200 ease-in-out bg-gray-800 text-white"
          />
        </div>

        <!-- End Date -->
        <div class="input-group">
          <label class="block mb-2 text-lg font-medium">تاریخ پایان</label>
          <input
            v-model="endDate"
            type="date"
            class="border border-gray-600 rounded-xl px-4 py-3 w-full focus:ring-2 focus:ring-orange-500 focus:outline-none transition duration-200 ease-in-out bg-gray-800 text-white"
          />
        </div>

        <!-- Export Button -->
        <button @click="handleExport" :disabled="loading" class="export-button">
          <span v-if="!loading">صدور داده‌های چت</span>
          <span v-else>در حال صدور...</span>
        </button>

        <!-- Message -->
        <p
          v-if="message"
          :class="{ 'text-green-500': success, 'text-red-500': !success }"
          class="text-center text-sm font-medium mt-4"
        >
          {{ message }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import config from "../config/featureConfig";
import { useRouter, useRoute } from "vue-router";
import axios from "axios";

const startDate = ref("");
const endDate = ref("");
const loading = ref(false);
const message = ref("");
const success = ref(false);
const persistKey = "export_dates";
const sidebarOpen = ref(true);
const router = useRouter();
const route = useRoute();
const currentRoute = route.path; // Get the current route path
const buttons = config.buttons.filter((btn) => btn.enabled);

onMounted(() => {
  const saved = localStorage.getItem(persistKey);
  if (saved) {
    const parsed = JSON.parse(saved);
    startDate.value = parsed.start || "";
    endDate.value = parsed.end || "";
  }
});

watch([startDate, endDate], ([newStart, newEnd]) => {
  localStorage.setItem(
    persistKey,
    JSON.stringify({
      start: newStart,
      end: newEnd,
    })
  );
});

const handleExport = async () => {
  if (!startDate.value || !endDate.value) {
    message.value = "لطفاً هر دو تاریخ را وارد کنید.";
    success.value = false;
    return;
  }

  const formData = new FormData();
  formData.append("start_date", startDate.value);
  formData.append("end_date", endDate.value);

  try {
    loading.value = true;
    message.value = "";

    const token =
      localStorage.getItem("access_token") || localStorage.getItem("token");
    const res = await fetch("http://localhost:8000/manage_data/export", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
      },
      body: formData,
    });

    const result = await res.json();
    loading.value = false;

    if (!res.ok) {
      throw new Error(result.detail || "صدور ناموفق بود");
    }

    message.value = `صادر شد! فایل: ${result.filename}`;
    success.value = true;
  } catch (err) {
    loading.value = false;
    message.value = `${err.message}`;
    success.value = false;
  }
};

const toggleSidebar = () => {
  sidebarOpen.value = !sidebarOpen.value;
};

const handleLogout = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("token");
  window.location.href = "/login";
};

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

const handleDashboard = () => {
  router.push("/dashboard");
};
</script>
