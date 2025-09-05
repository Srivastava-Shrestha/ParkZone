<template>
    <div class="app">
      <div class="container">
        <h1 class="heading"> Notifications</h1>
  
        <div class="notification-card"
             v-for="(notification, index) in notifications"
             :key="notification.notification_id"
             @click="toggleExpand(index)">
          <div class="card-header">
            <span class="notif-id">#{{ notification.notification_id }}</span>
            <span class="notif-title">{{ notification.title }}</span>
            <span class="arrow" :class="{ rotate: expandedIndex === index }">⌄</span>
          </div>
          <transition name="fade">
            <div class="card-body" v-if="expandedIndex === index" v-html="notification.body"></div>
          </transition>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { callApi } from '@/utils.js'
  
  const notifications = ref([])
  const expandedIndex = ref(null)
  
  const toggleExpand = (index) => {
    expandedIndex.value = expandedIndex.value === index ? null : index
  }
  
  const load_notifications = async () => {
    try {
      const { ok, resData } = await callApi('notification')
      if (ok) notifications.value = resData
      else alert(resData?.message || 'Unauthorized')
    } catch (err) {
      console.error('Error loading notifications:', err)
    }
  }
  
  onMounted(load_notifications)
  </script>
  
  <style scoped>
  .app {
    min-height: 100vh;
    padding: 40px 20px;
    font-family: 'Segoe UI', sans-serif;
  }
  
  .container {
    max-width: 1000px;
    margin: 50px;
  }
  
  .heading {
    font-size: 2.6rem;
    font-weight: 700;
    margin-bottom: 30px;
    border-left: 4px solid #38bdf8;
    padding-left: 12px;
  }
  
  .notification-card {
    backdrop-filter: blur(12px);
    border: 1px solid #475569;
    border-radius: 20px;
    padding: 18px 22px;
    margin-bottom: 20px;
    cursor: pointer;
    box-shadow: 0 0 8px rgba(56, 189, 248, 0.1);
    transition: all 0.25s ease-in-out;
  }
  
  .notification-card:hover {
    box-shadow: 0 0 18px rgba(56, 189, 248, 0.35);
    transform: translateY(-2px);
  }
  
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 600;
    font-size: 1rem;
  }
  

  .notif-title {
    flex: 1;
    text-align: left;
    margin-left: 10px;
    font-size: 1.05rem;
  }
  
  .arrow {
    transition: transform 0.2s ease;
    font-size: 1.2rem;
    color: #38bdf8;
  }
  .rotate {
    transform: rotate(180deg);
  }
  
  .card-body {
    margin-top: 16px;
    padding: 18px;
    border-radius: 12px;
    font-size: 0.97rem;
    line-height: 1.6;
    border-left: 3px solid #38bdf8;
  }
  

  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
    transform: translateY(-6px);
  }
  
  @media (max-width: 640px) {
    .card-header {
      flex-direction: column;
      align-items: flex-start;
      gap: 6px;
    }
    .notif-title {
      margin-left: 0;
    }
  }
  </style>
  