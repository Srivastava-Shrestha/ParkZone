<template>
    <div class="history-container container my-5">
      <div class="history-card p-4">
        <h3 class="mb-4 fw-bold">Parking History</h3>
        <div class="table-responsive">
          <table class="table table-borderless custom-table text-center align-middle">
            <thead>
              <tr class="mb-2">
                <th>Prime Location</th>
                <th>Spot ID</th>
                <th>Vehicle No.</th>
                <th>Parking Time</th>
                <th>Leaving Time</th>
                <th>Total Cost</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(history, index) in HistoryData" :key="index">
                <td>{{ history.prime_location }}</td>
                <td>{{ history.spot_id }}</td>
                <td>{{ history.vehicle_number }}</td>
                <td>{{ formatDate(history.parking_time) }}</td>
                <td>{{ formatDate(history.leaving_time) }}</td>
                <td>₹{{ history.parking_cost/100 }}</td>
                <td>
                  <span class="badge bg-secondary">Parked Out</span>
                </td>
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
  const formatDate = (datetime) => {
  if (!datetime) return '-'
  const date = new Date(datetime)
  return date.toLocaleString("en-IN", {
    day: "2-digit",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    hour12: true
  })
}
  const HistoryData = ref([])

  const ParkingHistory = async () => {
    try {
      const {ok, status, resData} = await callApi("reservation?payment_status=true")
    if (ok) {
      HistoryData.value = resData
    } else {
      alert(resData?.message || "Something went wrong! ")
    }
    } catch (err) {
      console.log(err)
    }
    
  }
  
  onMounted(ParkingHistory)
  </script>
  
  <style scoped>
  .history-card {
    background: transparent;
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 1rem;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.277);
    color: var(--text-primary);
  }
  
  .custom-table {
    background-color: transparent;
  }
  
  .custom-table thead th {
    padding-bottom: 1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }
  
  .custom-table tbody tr {
    line-height: 2.5rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  }
  
  .custom-table td, .custom-table th {
    background-color: transparent !important;
    color: var(--text-primary);
  }
  
  .badge {
    font-size: 0.9rem;
    padding:10px;
    border-radius: 1rem;
  }
  </style>
  