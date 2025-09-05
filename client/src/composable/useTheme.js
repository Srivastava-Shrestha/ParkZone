import { ref, reactive, watch } from 'vue'

// Global theme state
export const isDark = ref(false)


// Update body class for dark mode
const updateBodyClass = () => {
  if (isDark.value) {
    document.body.classList.add('dark')
  } else {
    document.body.classList.remove('dark')
  }
}

// Theme management functions
export const toggleDarkMode = () => {
  isDark.value = !isDark.value
  localStorage.setItem('darkMode', isDark.value.toString())
  updateBodyClass()
}

// Initialize theme system
export const initializeTheme = () => {
  // Load saved preferences
  const savedDarkMode = localStorage.getItem('darkMode')  
  if (savedDarkMode) {
    isDark.value = savedDarkMode === 'true'
  }
  updateBodyClass()
}

// Watch for theme changes
watch(isDark, updateBodyClass)