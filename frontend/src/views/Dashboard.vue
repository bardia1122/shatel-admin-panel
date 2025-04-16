<template>
  <div class="dashboard">
    <h1>Welcome to the Admin Panel</h1>
    <div class="button-group">
      <button>A</button>
      <button>B</button>
      <button>C</button>
      <button>D</button>
    </div>
  </div>
</template>

<script setup>
// Add any logic here if needed later
</script>

<style scoped>
.dashboard {
  padding: 4rem;
  text-align: center;
}

.button-group {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-top: 2rem;
}

button {
  padding: 1rem 2rem;
  font-size: 1.2rem;
  border: none;
  background: #4e54c8;
  color: white;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s ease;
}

button:hover {
  background: #3b4099;
}
</style>
