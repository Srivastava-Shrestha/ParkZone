<template>
    <div class="app-container">
      <Sidebar />
      <div class="main-panel">
        <Topbar />
        <div class="main-content">
           <router-view/>

        </div>
      </div>
    </div>
</template>

<script setup>
import Sidebar from '@/components/SideBar.vue'
import Topbar from '@/components/TopBar.vue'
// import Dashboard from './components/Dashboard.vue'
</script>

<style scoped>


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
  color: var(--text-primary);
  background-color: var(--bg-secondary);
  padding: 2rem;
  min-height: 100%;
  font-family: 'Inter', sans-serif;
  width: 100%;
}

</style>