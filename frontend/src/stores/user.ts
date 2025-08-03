import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

// Define user store
export const useUserStore = defineStore('user', () => {
  // User state
  const userInfo = ref<{id: string, username: string} | null>(null);

  // Derive isLoggedIn from userInfo
  const isLoggedIn = computed(() => userInfo.value !== null);

  // Set user information
  const setUserInfo = (userData: {id: string, username: string}) => {
    userInfo.value = userData;
    // Store user info in localStorage
    localStorage.setItem('userInfo', JSON.stringify(userData));
  };

  // Clear user information
  const clearUserInfo = () => {
    userInfo.value = null;
    localStorage.removeItem('userInfo');
  };

  // Initialize user from localStorage
  const initUser = () => {
    const savedUser = localStorage.getItem('userInfo');
    if (savedUser) {
      userInfo.value = JSON.parse(savedUser);
    }
  };

  return {
    userInfo,
    isLoggedIn,
    setUserInfo,
    clearUserInfo,
    initUser
  };
});
