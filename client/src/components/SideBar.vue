<template>
  <div class="sidebar-container">
    <div :class="['sidebar', { collapsed }]">
      <!-- Window Dots -->
      <div class="window-controls">
        <div class="dot-red"></div>
        <div class="dot-yellow"></div>
        <div class="dot-green"></div>
      </div>

      <!-- Brand -->
      <div class="brand">
        <div class="brand-icon">
          <img src="@/assets/logo-transparent.png" class="brand-icon-svg" />
        </div>
        <span class="text brand-name">ParkZone</span>
      </div>

      <!-- Menu -->
      <ul class="menu">
        <li 
          :class="{ active: activeItem === 'dashboard' }" 
          @click="() => { 
            setActiveItem('dashboard'); 
            router.push(role === 'admin' ? '/dashboard/admin-summary' : '/dashboard/user-summary') 
          }"
        >
          <LayoutDashboard class="menu-icon" />
          <span class="text">Dashboard</span>
        </li>
        <li :class="{ active: activeItem === 'parkinglot' }" v-if="role === 'admin'"  @click="() => { setActiveItem('parkinglot'); router.push('/dashboard/lot') }">
          <LandPlot class="menu-icon" />
          <span class="text">Parking Lot</span>
        </li>
        <li :class="{ active: activeItem === 'available_lots' }" v-if="role === 'user'"  @click="() => { setActiveItem('available_lots'); router.push('/dashboard/available_lots') }">
          <LandPlot class="menu-icon" />
          <span class="text">Available Lots</span>
        </li>

        <li :class="{ active: activeItem === 'users' }" v-if="role === 'admin'"  @click="() => { setActiveItem('users'); router.push('/dashboard/users') }">
          <Users class="menu-icon" />
          <span class="text">Users</span>
        </li>

        <li :class="{ active: activeItem === 'payments' }"  v-if="role === 'admin'" @click="() => { setActiveItem('payments'); router.push('/dashboard/payment') }">
          <IndianRupee class="menu-icon" />
          <span class="text">Payments</span>
        </li>
        <li :class="{ active: activeItem === 'parkinghistory' }"  v-if="role === 'user'" @click="() => { setActiveItem('parkinghistory'); router.push('/dashboard/parking-history') } ">
          <FolderClock class="menu-icon" />
          <span class="text">Parking History</span>
        </li>
        <li :class="{ active: activeItem === 'notifications' }" v-if="role === 'user'" @click="() => { setActiveItem('notifications'); router.push('/dashboard/notification')}">
          <Bell class="menu-icon" />
          <span class="text">Notifications</span>
        </li>
      </ul>

      <!-- Logout Section -->
      <div class="logout-section">
        <div class="user-profile" v-if="!collapsed">
          <Panda alt="User" class="user-avatar" />
          <div class="user-details">
            <span class="user-name">Hi {{ username}}! </span>
          </div>
        </div>
        <button class="logout-btn" @click="logout()" :title="collapsed ? 'Logout' : ''">
          <LogOut class="logout-icon" />
        </button>
      </div>
    </div>

    <!-- External Toggle Button -->
    <div class="sidebar-toggle" @click="toggleSidebar">
      <ChevronLeft class="toggle-icon" :class="{ rotated: collapsed }" />
    </div>
  </div>
  <Modal
      :is-open="showModal"
      @close="closeModal"
      >
   <Logout v-if="showLogoutModal" @confirm="ConfirmLogout" @cancel="closeModal"/>
  </Modal>
</template>

<script setup>
import { ref ,onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { dataStore } from '../store/data';
import Logout from '@/components/Logout.vue'
import {callApi, removeCookie} from '@/utils.js'
import Modal from '@/components/Modal.vue'

const router = useRouter()
const route = useRoute()
import { 
  Panda, 
  LayoutDashboard, 
  LandPlot, 
  Users, 
  FolderClock,
  SquareParking, 
  IndianRupee, 
  Bell, 
  LogOut, 
  ChevronLeft 
} from 'lucide-vue-next'



const collapsed = ref(false)
const classesOpen = ref(false)
const activeItem = ref('dashboard')
const currentStore = dataStore()
const role = currentStore.role
const username = currentStore.username

const toggleSidebar = () => {
  collapsed.value = !collapsed.value
}

const toggleClasses = () => {
  classesOpen.value = !classesOpen.value
}

const setActiveItem = (item) => {
  activeItem.value = item
}
const showModal = ref(false)
const showLogoutModal = ref(false)

function logout () {
  showModal.value = true
  showLogoutModal.value = true
}

const ConfirmLogout = async () => {
  try{
      removeCookie("access_token_cookie")
      router.push('/login')
    } 
   catch (err) {
    console.log(err)
  }
}
function closeModal () {
  showModal.value = false
  showLogoutModal.value = false
}


onMounted(() => {
  const current = route.path
  if (current.includes('/dashboard/lot')) {
    setActiveItem('parkinglot')
  } else if (current.includes('/dashboard/users')) {
    setActiveItem('users')
  } else if (current.includes('/dashboard/available_lots')) {
    setActiveItem('available_lots')
  }
   else if (current.includes('/dashboard/payment')) {
    setActiveItem('payments')
  }else if (current.includes('/dashboard/parking-history')) {
    setActiveItem('parkinghistory')
  } else if (current.includes('/dashboard/notification')) {
    setActiveItem('notifications')
  } else if (current === '/dashboard') {
    setActiveItem('dashboard')
  }
})



defineExpose({
  collapsed
})
</script>

<style scoped>
.sidebar-container {
  position: relative;
  display: flex;
  align-items: flex-start;
}

.sidebar {
  width: 260px;
  background-color: var(--bg-primary);
  padding: 20px;
  color: var(--text-primary);
  transition: all 0.3s ease;
  height: 100vh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  border: 1px solid var(--border-primary);
  border-left: none;
  border-top: none;
  border-bottom: none;
}

.sidebar.collapsed {
  width: 80px;
  padding: 20px 15px;
}

.window-controls {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
  min-height: 12px;
  align-items: center;
  flex-shrink: 0;
}

.sidebar.collapsed .window-controls {
  justify-content: center;
  gap: 6px;
}

.window-controls div {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  flex-shrink: 0;
  transition: none;
}

.dot-red { 
  background-color: #ff5f56;
}
.dot-yellow { 
  background-color: #ffbd2e;
}
.dot-green { 
  background-color: #27c93f;
}

.brand {
  display: flex;
  align-items: center;
  margin-bottom: 30px;
  gap: 12px;
  min-height: 40px;
}

.sidebar.collapsed .brand {
  justify-content: center;
}

.brand-icon {
  width: 40px;
  height: 40px;
  /* background: linear-gradient(135deg, var(--theme-primary), var(--theme-secondary)); */
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.2rem;
  flex-shrink: 0;
}

.brand-icon-svg {
  width: 40px;
  height: 40px;
}

.brand-name {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--text-primary);
}

.menu {
  list-style: none;
  padding-left: 0;
  flex: 1;
  margin-bottom: 20px;
}

.menu li {
  display: flex;
  align-items: center;
  padding: 10px;
  color: var(--text-secondary);
  border-radius: 8px;
  margin-bottom: 5px;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
}

.menu li:hover::before,
.menu li.active::before {
  opacity: 1;
}

.sidebar.collapsed .menu li {
  justify-content: center;
}

.sidebar.collapsed .menu li::before {
  left: -15px;
}

.menu li:hover,
.menu li.active {
  background-color: var(--bg-secondary);
  border-left: 3px solid var(--theme-primary);
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
  padding-left: 12px;
  color: var(--text-primary);
}

.menu-icon {
  margin-right: 10px;
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.sidebar.collapsed .menu-icon {
  margin-right: 0;
}

.menu li .badge {
  margin-left: auto;
  background-color: var(--theme-primary);
  color: white;
  font-size: 0.75rem;
  padding: 2px 6px;
  border-radius: 8px;
}

.logout-section {
  margin-top: auto;
  padding-top: 20px;
  border-top: 1px solid var(--border-primary);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  min-height: 60px;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 12px;
  flex: 1;
}

.user-avatar {
  width: 25px;
  height: 25px;
  /* border-radius: 50%; */
  object-fit: cover;
  flex-shrink: 0;
  /* border: 2px solid var(--theme-primary); */
}

.user-details {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.user-name {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-primary);
}

.logout-btn {
  background: var(--bg-secondary);
  border: 1px solid var(--border-primary);
  color: var(--text-primary);
  padding: 8px;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  flex-shrink: 0;
  width: 36px;
  height: 36px;
}

.logout-icon {
  width: 18px;
  height: 18px;
}

.logout-btn:hover {
  background: #b91c1c;
  color: white;
  border-color: #b91c1c;
}

.sidebar-toggle {
  position: absolute;
  top: 60px;
  right: -12px;
  background: linear-gradient(135deg, var(--theme-primary), var(--theme-secondary));
  border-radius: 50%;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: white;
  font-weight: bold;
  transition: all 0.3s ease;
  box-shadow: var(--shadow-md);
  z-index: 9999;
}

.sidebar-toggle:hover {
  background: linear-gradient(135deg, var(--theme-secondary), var(--theme-primary));
  transform: scale(1.1);
}

.toggle-icon {
  transition: transform 0.3s ease;
  width: 14px;
  height: 14px;
}

.toggle-icon.rotated {
  transform: rotate(180deg);
}

.collapsed .text,
.collapsed .badge {
  display: none;
}

.collapsed .user-details {
  display: none;
}

.collapsed .logout-section {
  justify-content: center;
}

.collapsed .user-profile {
  justify-content: center;
  flex: none;
}
</style>