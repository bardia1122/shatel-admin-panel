<script setup>
import { useRouter } from 'vue-router'
import config from '../config/featureConfig'

const router = useRouter()
const buttons = config.buttons.filter(btn => btn.enabled)

const navigate = (route) => {
  router.push(route)
}

</script>

<template>
    <div class="dashboard-container">
      <div class="grid-and-text">
        <div class="button-grid">
          <button v-for="btn in buttons" :key="btn.key" @click="navigate(btn.route)">
            {{ btn.label }}
          </button>
        </div>
        <div class="welcome-text">
          <h1>به پنل ادمین خوش آمدید</h1>
        </div>
      </div>
    </div>
  </template>

  
  <style scoped>
  .dashboard-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: white;
    font-family: 'B Nazanin', sans-serif;
  }
  
  .grid-and-text {
    display: flex;
    gap: 4rem;
    align-items: center;
  }
  
  .button-grid {
    display: grid;
    grid-template-columns: repeat(2, 192px);
    grid-template-rows: repeat(2, 100px);
    gap: 1.5rem;
  }
  
  .button-grid button {
    width: 100%;
    height: 100%;
    font-size: 1.5rem;
    font-weight: bold;
    border: none;
    border-radius: 12px;
    background-color: #002f6c;
    color: white;
    cursor: pointer;
    padding: 0.5rem;
    transition: background-color 0.3s;
    text-align: center;
    line-height: 1.5;
  }
  
  .button-grid button:hover {
    background-color: #f26522;
    transform: translateY(-2px);
    box-shadow: 0 8px 16px rgba(242, 101, 34, 0.4);
  }
  
  .welcome-text h1 {
    font-size: 2.2rem;
    color: #002f6c;
    max-width: 280px;
    text-align: center;
  }
  </style>
  