<template>
    <div class="app">
      <div class="container">
        <div class="header">
          <h1 class="title">User Information</h1>
          <p class="subtitle">Manage and view user details</p>
        </div>
        <div class="table-container">
          <table class="user-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>E_Mail</th>
                <th>Full name</th>
                <th>Address</th>
                <th>Pin code</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in users" :key="user.user_id">
                <td>{{ user.user_id }}</td>
                <td>{{ user.email }}</td>
                <td>{{ user.username}}</td>
                <td>{{ user.address }}</td>
                <td>{{ user.pincode }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { callApi } from '@/utils.js'
  

  
  const users = ref([])
  const load_users = async () => {
  try {
    const {ok, status, resData} = await callApi('user');
    if (ok) {
      users.value = resData
    } else {
      alert(resData?.message || "Unauthorized")
      console.warn("Error fetching users:", resData);
    }
    
  } catch (err) {
    console.error("Exception while loading users:", err);
  }
   
  };
  
  onMounted(load_users) 

  </script>
  
  <style scoped>
  .app {
    min-height: 100vh;
    padding: 40px 20px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .header {
    text-align: center;
    margin-bottom: 40px;
  }
  
  .title {
    font-size: 3rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 10px;
    letter-spacing: -0.02em;
  }
  
  .subtitle {
    font-size: 1.2rem;
    color: var(--text-primary);
    font-weight: 300;
    margin: 0;
  }
  
  .table-container {
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.292);
    border: 1px solid rgba(255, 255, 255, 0.312);
  }
  
  .user-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 16px;
  }
  
  .user-table th {
    color: var(--text-primary);
    padding: 20px 25px;
    text-align: left;
    font-weight: 700;
    font-size: 15px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 1px solid rgba(0, 0, 0, 0.442);
  }
  
  .user-table td {
    padding: 18px 25px;
    font-size: 16px;
    font-weight: 500;
    color: var(--text-primary);
    border-bottom: 1px solid rgba(0, 0, 0, 0.119);
    transition: all 0.4s ease;
  }
  
  .user-table tbody tr {
    transition: all 0.3s ease;
    cursor: pointer;
  }
  
  .user-table tbody tr:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(11, 10, 10, 0.345);
  }
  
  .user-table tbody tr:last-child td {
    border-bottom: none;
  }
  
  /* Responsive */
  @media (max-width: 768px) {
    .title {
      font-size: 2.5rem;
    }
  
    .subtitle {
      font-size: 1.1rem;
    }
  
    .user-table th,
    .user-table td {
      padding: 15px 18px;
      font-size: 14px;
    }
  }
  
  @media (max-width: 480px) {
    .title {
      font-size: 2rem;
    }
  
    .subtitle {
      font-size: 1rem;
    }
  
    .user-table th,
    .user-table td {
      padding: 12px 15px;
      font-size: 13px;
    }
  }
  </style>
  