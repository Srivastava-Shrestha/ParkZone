<template>
  <div class="topbar">
    <div class="topbar-container">
      <!-- Page -->
      <div class="brand">
        <span class="brand-text">{{ brandTitle }}</span>
      </div>


      <!-- Actions -->
      <div class="actions">

        <!-- Dark Mode Toggle -->
        <button 
          class="action-btn dark-mode-btn"
          @click="toggleDarkMode"
          :aria-label="isDark ? 'Switch to light mode' : 'Switch to dark mode'"
        >
          <Sun v-if="isDark" class="icon" />
          <Moon v-else class="icon" />
        </button>


        <!-- User Profile -->
        <div class="user-profile" ref="userProfile">
          <button 
            class="profile-btn"
            aria-label="User menu"
          >
            <img 
              src="@/assets/boww.png" 
              alt="User Avatar"
              class="avatar"
            />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { 
  Sun,
  Moon
} from 'lucide-vue-next'
import { 
  isDark, 
  toggleDarkMode,
} from '@/composable/useTheme.js'

import { computed } from 'vue'
import { useRoute } from 'vue-router'


const route = useRoute()

const brandTitle = computed(() => {
  const map = {
    '/dashboard': 'Dashboard',
    '/dashboard/admin-summary': 'Dashboard',
    '/dashboard/user-summary': 'Dashboard',
    '/dashboard/lot': 'Parking Lots',
    '/dashboard/available_lots': 'Available Lots',
    '/dashboard/users': 'Users',
    '/dashboard/payment': 'Payments',
    '/dashboard/parking-history': 'Parking History',
    '/dashboard/notification': 'Notifications'
  }
  return map[route.path] || 'ParkZone'
})


</script>

<style scoped>
.topbar {
  background: var(--bg-primary);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--border-primary);
  z-index: 100;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  flex-shrink: 0;
}

.topbar-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
}

/* Brand */
.brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-text {
  font-size: 20px;
  font-weight: 700;
  color: var(--theme-primary);
  transition: color 0.3s ease;
}

/* Search */
.search-container {
  flex: 1;
  max-width: 480px;
  margin: 0 32px;
}

.search-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.search-icon {
  position: absolute;
  left: 12px;
  width: 20px;
  height: 20px;
  color: var(--text-tertiary);
  transition: color 0.3s ease;
  z-index: 1;
}

.search-input {
  width: 100%;
  padding: 12px 16px 12px 44px;
  border: 1px solid var(--border-primary);
  border-radius: 12px;
  background: var(--bg-primary);
  color: var(--text-primary);
  font-size: 14px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.search-input:focus {
  outline: none;
  border-color: var(--theme-primary);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.search-input:focus + .search-icon {
  color: var(--theme-primary);
}

/* Actions */
.actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border: none;
  border-radius: 10px;
  background: transparent;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
}

.action-btn:hover {
  background: rgba(59, 130, 246, 0.1);
  color: var(--theme-primary);
  transform: translateY(-1px);
}

.action-btn.active {
  background: var(--theme-primary);
  color: white;
}

.icon {
  width: 20px;
  height: 20px;
}

/* Dark Mode Toggle Switch */
.dark-mode-toggle {
  cursor: pointer;
  user-select: none;
}

.toggle-track {
  position: relative;
  width: 60px;
  height: 32px;
  background: var(--bg-tertiary);
  border: 2px solid var(--border-primary);
  border-radius: 20px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 6px;
  overflow: hidden;
}

.toggle-track.active {
  background: var(--theme-primary);
  border-color: var(--theme-primary);
}

.toggle-thumb {
  position: absolute;
  width: 24px;
  height: 24px;
  background: white;
  border-radius: 50%;
  left: 2px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  z-index: 2;
}

.toggle-thumb.active {
  left: 32px;
  background: #1e293b;
}

.toggle-icon {
  width: 14px;
  height: 14px;
  transition: all 0.3s ease;
}

.sun-icon {
  color: #f59e0b;
}

.moon-icon {
  color: #e5e7eb;
}

.track-icon {
  width: 16px;
  height: 16px;
  z-index: 1;
  transition: all 0.3s ease;
}

.sun-track {
  color: #f59e0b;
  opacity: 1;
}

.moon-track {
  color: #e5e7eb;
  opacity: 1;
}

.toggle-track.active .sun-track {
  opacity: 0.3;
}

.toggle-track:not(.active) .moon-track {
  opacity: 0.3;
}

/* Theme Selector */
.theme-selector {
  position: relative;
}

.theme-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 8px;
  width: 240px;
  background: var(--bg-primary);
  border: 1px solid var(--border-primary);
  border-radius: 12px;
  box-shadow: var(--shadow-lg);
  z-index: 1000;
  animation: slideDown 0.2s ease;
}

.theme-dropdown-header {
  padding: 16px;
  border-bottom: 1px solid var(--border-primary);
  font-weight: 600;
  color: var(--text-primary);
}

.theme-options {
  padding: 8px;
}

.theme-option {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: var(--text-primary);
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: left;
}

.theme-option:hover {
  background: var(--bg-tertiary);
}

.theme-option.active {
  background: rgba(59, 130, 246, 0.1);
  color: var(--theme-primary);
}

.theme-color {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 2px solid var(--bg-primary);
  box-shadow: var(--shadow-sm);
}

.check-icon {
  width: 16px;
  height: 16px;
  margin-left: auto;
  color: var(--theme-primary);
}

/* Notifications */
.notification-container {
  position: relative;
}

.notification-badge {
  position: absolute;
  top: -2px;
  right: -2px;
  background: #EF4444;
  color: white;
  font-size: 11px;
  font-weight: 600;
  min-width: 18px;
  height: 18px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid var(--bg-primary);
  animation: pulse 2s infinite;
}

/* User Profile */
.user-profile {
  position: relative;
}

.profile-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 4px 8px 4px 4px;
  border: none;
  border-radius: 24px;
  background: transparent;
  cursor: pointer;
  transition: all 0.2s ease;
}

.profile-btn:hover {
  background: rgba(59, 130, 246, 0.1);
}

.profile-btn.active {
  background: rgba(59, 130, 246, 0.1);
}

.avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  object-fit: cover;
  /* border: 2px solid var(--theme-primary); */
}

.chevron {
  width: 16px;
  height: 16px;
  color: var(--text-secondary);
  transition: transform 0.2s ease;
}

.profile-btn.active .chevron {
  transform: rotate(180deg);
}

.user-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 8px;
  width: 280px;
  background: var(--bg-primary);
  border: 1px solid var(--border-primary);
  border-radius: 12px;
  box-shadow: var(--shadow-lg);
  z-index: 1000;
  animation: slideDown 0.2s ease;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
}

.user-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid var(--theme-primary);
}

.user-details {
  flex: 1;
}

.user-name {
  display: block;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 2px;
}

.user-email {
  display: block;
  font-size: 14px;
  color: var(--text-secondary);
}

.dropdown-divider {
  height: 1px;
  background: var(--border-primary);
  margin: 8px 0;
}

.dropdown-menu {
  padding: 8px;
}

.dropdown-item {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: var(--text-primary);
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: left;
}

.dropdown-item:hover {
  background: var(--bg-tertiary);
}

.dropdown-item.logout {
  color: #EF4444;
}

.dropdown-item.logout:hover {
  background: rgba(239, 68, 68, 0.1);
}

.dropdown-icon {
  width: 18px;
  height: 18px;
}

/* Animations */
@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .topbar-container {
    padding: 0 16px;
  }
  
  .search-container {
    max-width: 200px;
    margin: 0 16px;
  }
  
  .brand-text {
    display: none;
  }
  
  .actions {
    gap: 4px;
  }
  
  .action-btn {
    width: 36px;
    height: 36px;
  }
  
  .theme-dropdown,
  .user-dropdown {
    width: 220px;
  }
}

@media (max-width: 480px) {
  .search-container {
    display: none;
  }
  
  .topbar-container {
    justify-content: space-between;
  }
}
</style>