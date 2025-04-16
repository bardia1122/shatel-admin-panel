<template>
  <div class="login-wrapper">
    <div class="login-card">
      <h2>Admin Panel Login</h2>
      <form @submit.prevent="handleLogin">
        <input v-model="username" placeholder="Username" required />
        <input v-model="password" type="password" placeholder="Password" required />
        <button type="submit">Login</button>
        <p v-if="error" class="error">{{ error }}</p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      username: '',
      password: '',
      error: null
    }
  },
  methods: {
    async handleLogin() {
        this.error = null
        try {
            const response = await axios.post('http://localhost:8000/login', new URLSearchParams({
            username: this.username,
            password: this.password
            }))
            localStorage.setItem('token', response.data.access_token)
            this.$router.push('/dashboard') // redirect
        } catch (err) {
            this.error = err.response?.data?.detail || 'Login failed'
        }
    }

  }
}
</script>

<style scoped>
.login-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  padding: 2rem;
  background: linear-gradient(to bottom right, #002147, #ccd3db);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.login-card {
  background: white;
  padding: 3rem 4rem;
  border-radius: 16px;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.25);
  width: 100%;
  max-width: 500px;
  min-width: 400px;
  text-align: center;
}

.login-card h2 {
  margin-bottom: 2.5rem;
  font-size: 1.8rem;
  color: #2c2c2c;
}

.login-card input {
  width: 100%;
  padding: 1rem;
  margin-bottom: 1.5rem;
  border-radius: 10px;
  border: 1px solid #ccc;
  font-size: 1.2rem;
  transition: border-color 0.3s;
}

.login-card input:focus {
  border-color: #4e54c8;
  outline: none;
}

.login-card button {
  width: 100%;
  padding: 1rem;
  background: #002f6c;
  color: white;
  font-size: 1rem;
  font-weight: bold;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.login-card button:hover {
  background: #f26522;
}

.error {
  margin-top: 1rem;
  color: red;
  font-size: 1.1rem;
}
</style>
