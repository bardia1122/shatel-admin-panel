<template>
  <div class="login-wrapper">
    <div class="login-card">
      <h2>ورود به پنل ادمین</h2>
      <form @submit.prevent="handleLogin">
        <label>نام کاربری</label>
        <input v-model="username" required />
        <label>رمز عبور</label>
        <input v-model="password" type="password" required />
        <button type="submit">ورود</button>
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
            console.log("Token being sent:", response.data.access_token)
            this.$router.push('/dashboard') // redirect
        } catch (err) {
            console.log(err)
            this.error = err.response?.data?.detail || 'Login failed'
        }
    }

  }
}
</script>

