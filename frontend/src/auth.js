export const useAuth = () => {
    return {
      getToken() {
        const token = localStorage.getItem("token");
        if (!token) {
          console.error("Authentication token is missing!");
          return null;
        }
        return token;
      },
  
      setToken(token) {
        localStorage.setItem("token", token);
      },
  
      removeToken() {
        localStorage.removeItem("authToken");
      },
    };
  };

  export function getTokenPermissions() {
    const token = localStorage.getItem('token')
    if (!token) return []
    try {
      const payload = JSON.parse(atob(token.split('.')[1]))
      return payload.permissions || []
    } catch (err) {
      console.error("Failed to decode token:", err)
      return []
    }
  }
  