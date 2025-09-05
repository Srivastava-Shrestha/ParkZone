<script setup>

import { onMounted } from 'vue'
import Admin from './Dashboard/Admin.vue';
import User from './Dashboard/User.vue';
import { dataStore } from '../store/data';
import { isDark, initializeTheme } from '@/composable/useTheme.js';


const data_store = dataStore()
const role = data_store.role

onMounted(() => {
  initializeTheme()
})

</script>

<template>
    <div class="app" :class="{ 'dark': isDark }">
    <Admin v-if="role === 'admin'"/>
    <User v-if="role === 'user'"/>
    </div>
</template>

<style scoped>
.app {
    min-height: 100vh;
    background-color: var(--bg-secondary);
    color: var(--text-primary);
    transition: background-color 0.3s ease;
    padding: 0;
    margin: 0;
    
  }
  

</style>