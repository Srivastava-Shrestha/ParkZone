<template>
    <div class="payment-wrapper">
      <div class="payment-container">
        <header class="payment-header">
          <h1>Payment Records</h1>
          <p>Overview of all completed transactions</p>
        </header>
  
        <section class="payment-table-wrapper">
          <table class="payment-table">
            <thead>
              <tr>
                <th>User ID</th>
                <th>Username</th>
                <th>Email</th>
                <th>Spot ID</th>
                <th>Total Paid (₹)</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="record in Userpayments" :key="record.user_id + '-' + record.spot_id">
                <td>{{ record.user_id }}</td>
                <td>{{ record.username }}</td>
                <td>{{ record.email }}</td>
                <td>{{ record.spot_id }}</td>
                <td>₹ {{ (record.parking_cost / 100) }}</td>
              </tr>
            </tbody>
          </table>
        </section>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { callApi } from '@/utils.js'
  
  const Userpayments = ref([])
  
  const loadPayments = async () => {
    try {
      const { ok, resData } = await callApi('reservation?payment_status=true')
      if (ok) {
        Userpayments.value = resData
      } else {
        console.warn("Failed to fetch payment details:", resData)
        alert(resData?.message || "Failed to load")
      }
    } catch (err) {
      console.error("Error loading payment data:", err)
    }
  }
  
  onMounted(loadPayments)
  </script>
  
  <style scoped>
.payment-wrapper {
  padding: 3rem 1.5rem;
  background-color: var(--bg-secondary);
  min-height: 100vh;
  font-family: 'Segoe UI', sans-serif;
}

.payment-container {
  max-width: 1100px;
  margin: auto;
}

.payment-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.payment-header h1 {
  font-size: 2.75rem;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 0.4rem;
  letter-spacing: -0.5px;
}

.payment-header p {
  font-size: 1.15rem;
  color: var(--text-secondary);
  font-weight: 400;
  opacity: 0.85;
}

.payment-table-wrapper {
  background: var(--bg-primary);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
  transition: box-shadow 0.3s ease;
}

.payment-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95rem;
}

.payment-table thead {
  background: rgba(255, 255, 255, 0.04);
}

.payment-table th,
.payment-table td {
  padding: 18px 24px;
  text-align: left;
  color: var(--text-primary);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  transition: background-color 0.2s ease;
}

.payment-table th {
  text-transform: uppercase;
  font-weight: 700;
  font-size: 0.85rem;
  letter-spacing: 0.7px;
  color: var(--text-secondary);
}

.payment-table tbody tr:hover {
  background-color: rgba(255, 255, 255, 0.02);
  cursor: pointer;
}

.payment-table tbody tr:last-child td {
  border-bottom: none;
}

  </style>
  