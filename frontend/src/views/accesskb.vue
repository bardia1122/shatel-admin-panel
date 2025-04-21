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
          <h2>دسترسی به پایگاه دانش</h2>
  
          <!-- Drag and Drop File Upload -->
          <div
            class="upload-area"
            @dragover.prevent
            @drop.prevent="handleDrop"
          >
            <p v-if="!file">فایل خود را اینجا رها کنید یا کلیک کنید</p>
            <p v-else>فایل انتخاب شده: {{ file.name }}</p>
            <input type="file" @change="handleFileChange" hidden ref="fileInput" />
            <button @click="$refs.fileInput.click()">انتخاب فایل</button>
          </div>
  
          <!-- Upload Button -->
          <button
            @click="uploadFile"
            :disabled="!file || loading"
            class="export-button"
          >
            <span v-if="!loading">بارگذاری فایل</span>
            <span v-else>در حال بارگذاری...</span>
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
  import { ref } from "vue";
  import config from "../config/featureConfig";
  import { useRouter, useRoute } from "vue-router";
  import axios from 'axios'

  const sidebarOpen = ref(true);
  const file = ref(null);
  const message = ref("");
  const success = ref(false);
  const loading = ref(false);
  const router = useRouter();
  const route = useRoute();
  const currentRoute = route.path;
  const buttons = config.buttons.filter((btn) => btn.enabled);
  
  const handleFileChange = (event) => {
    file.value = event.target.files[0];
  };
  
  const handleDrop = (event) => {
    const droppedFiles = event.dataTransfer.files;
    if (droppedFiles.length) {
      file.value = droppedFiles[0];
    }
  };
  
  const uploadFile = async () => {
    if (!file.value) return;
  
    const formData = new FormData();
    formData.append("file", file.value);
  
    try {
      loading.value = true;
      message.value = "";
  
      const token =
        localStorage.getItem("access_token") || localStorage.getItem("token");
  
      const res = await fetch("http://localhost:8000/access_kb/upload", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
        },
        body: formData,
      });
  
      const result = await res.json();
      loading.value = false;
  
      if (!res.ok) {
        throw new Error(result.detail || "خطا در بارگذاری فایل");
      }
  
      message.value = `بارگذاری موفقیت‌آمیز بود: ${result.filename || "فایل ارسال شد"}`;
      success.value = true;
    } catch (err) {
      console.error("Navigation error:", error)
      loading.value = false;
      message.value = err.message;
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
  

  