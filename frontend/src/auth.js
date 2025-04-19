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
  