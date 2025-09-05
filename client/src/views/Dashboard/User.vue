<template>
    <div class="app" :class="{ 'dark': isDark }">
      <div class="app-container">
        <Sidebar />
        <div class="main-panel">
          <Topbar />
          <div class="main-content">
            <!-- <Dashboard /> -->
            <router-view/>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue'
    import Sidebar from '@/components/SideBar.vue'
    import Topbar from '@/components/TopBar.vue'
//   import Dashboard from './components/Dashboard.vue'
  import { isDark, initializeTheme } from '@/composable/useTheme.js'
  
  onMounted(() => {
    initializeTheme()
  })
  </script>
  
  <style scoped>
  .app {
    min-height: 100vh;
    background-color: var(--bg-secondary);
    transition: background-color 0.3s ease;
    padding: 0;
    margin: 0;
  }
  
  .app-container {
    display: flex;
    height: 100vh;
    width: 100vw;
  }
  
  .main-panel {
    flex: 1;
    display: flex;
    flex-direction: column;
    background-color: var(--bg-primary);
    overflow: hidden;
  }
  
  .main-content {
    flex: 1;
    overflow-y: auto;
    overflow-x: hidden;
    background-color: var(--bg-secondary);
  }
  </style>