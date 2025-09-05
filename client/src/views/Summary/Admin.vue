<template>
    <div class="dashboard container py-2">
      <h2 class="fw-bold mb-4 dash">
        Parking Insights<ArrowBigRightDash/></h2>
      <!-- Info Cards -->
      <div class="row g-4 mb-4">
        <div class="col-md-3" v-for="card in cards" :key="card.label">
          <div class="card glass-card p-3 d-flex flex-row align-items-center">
            <component :is="card.icon" class="me-3 " size="36" :style="{ color: card.color }" />
            <div>
              <h6 class="mb-0 fw-semibold card-s">{{ card.label }}</h6>
              <h4 class="fw-bold">{{ card.value }}</h4>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Charts Section -->
      <div class="row g-4">
        <div class="col-md-6">
          <div class="card glass-card p-4">
            <h6 class="fw-semibold mb-3">Spots Distribution per Lot</h6>
            <canvas id="barChart" class="bar-chart"></canvas>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card glass-card p-4">
            <h6 class="fw-semibold mb-3">Booking Status</h6>
            <canvas id="pieChart"></canvas>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted, reactive, ref, computed } from 'vue'
  import { ParkingSquare, ParkingCircle, SquareSigma, IndianRupee, ArrowBigRightDash } from 'lucide-vue-next'
  import Chart from 'chart.js/auto'
  import {callApi} from '@/utils.js'


  const lotDetails = ref([])
  const lots = async () => {
    try {
      const {ok, status, resData } = await callApi('lot')
      if (ok) {
        lotDetails.value = resData
      } else {
        alert(resData?.message || "No Lots fetch!")
      }
    } catch (err) {
      console.log(err)
    }
  }
  const ReservationDetails = ref([])
  const Reservations = async () => {
    try {
      const {ok, status, resData } = await callApi('reservation?payment_status=true')
      if (ok) {
        ReservationDetails.value = resData
      } else {
        alert(resData?.message || "No Reservations fetch!")
      }
    } catch (err) {
      console.log(err)
    }
  }
  const ReservationPerLot = ref({})
  const adminStats = async () => {
    try {
      const {ok, status, resData } = await callApi('stats')
      if (ok) {
        ReservationPerLot.value = resData
      } else {
        alert(resData?.message || "No Reservations fetch!")
      }
    } catch (err) {
      console.log(err)
    }
  }
  
  const cards = computed(() => [
  { label: 'Lots Created', value: lotDetails.value.length, icon: ParkingSquare, color: '#3b82f6' },
  { label: 'Available Spots', value:lotDetails.value.reduce((total, lot) => total + lot.spots.filter(spot => spot.status).length,0)
  , icon: ParkingCircle, color: '#f59e0b' },
    { label: 'Total Earnings', value:`₹ ${ReservationDetails.value.reduce((sum, res) => sum + (res.parking_cost/100 || 0), 0).toLocaleString('en-IN')}`, icon: IndianRupee, color: '#22c55e' },
    { label: 'Total Reservations', value: ReservationDetails.value.length, icon: SquareSigma, color: '#ef4444' },
  ])
  
  onMounted( async() => {
    await lots();
    await Reservations();
    await adminStats();
    const allSpots = lotDetails.value.flatMap(lot => lot.spots || [])
    const pieData1 = allSpots.filter(spot => spot.status).length     
    const pieData2 = allSpots.filter(spot => !spot.status).length    
    new Chart(document.getElementById('barChart'), {
  type: 'bar',
  data: {
    labels:Object.keys(ReservationPerLot.value),
    datasets: [
      {
        label: 'Reservations',
        data: Object.values(ReservationPerLot.value),
        backgroundColor: [
      'rgba(255, 99, 132, 0.8)',
      'rgba(255, 159, 64, 0.8)',
      'rgba(75, 192, 192, 0.8)',
      'rgba(54, 162, 235, 0.8)'
    ],
    borderColor: [
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)'
    ],
        barThickness: 60,
        borderRadius: 6
      }
    ]
  },
  options: {
    responsive: true,
    plugins: {
      legend: { display: false },
      labels: {
        color: '#64748b'},
      title: {
        display: true,
        text: 'Reservations per Lot',
        color:"#64748b",
        font: { size: 16, weight: 'bold' }
      }
    },
    scales: {
    x: {
      title: {
        display: true,
        text: 'Lots',
        color: "#64748b",
        font: { size: 16, weight: 'bold' }
      },
      ticks: {
        color: '#64748b',
        font: { size: 14 }
      }
    },
    y: {
      beginAtZero: true,
      title: {
        display: true,
        text: 'Number of Reservations',
        color: "#64748b",
        font: { size: 16, weight: 'bold' }
      },
      ticks: {
        color: '#64748b',
        font: { size: 14 }
      }
    }
  }}
})
  
new Chart(document.getElementById('pieChart'), {
  type: 'pie',
  data: {
    labels: ['Booked', 'Available'],
    datasets: [{
      data: [pieData2, pieData1],
      backgroundColor: ['#ffb5a7', '#caffbf'] 
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'bottom',
        labels: {
          generateLabels: function (chart) {
            const data = chart.data;
            return data.labels.map((label, i) => ({
              text: label,
              fillStyle: data.datasets[0].backgroundColor[i],
              strokeStyle: data.datasets[0].backgroundColor[i],
              lineWidth: 1,
              hidden: false,
              index: i,
              fontColor: label === 'Booked' ? '#dc2626' : '#16a34a'
            }));
          },
          color: (ctx) => {
            const label = ctx.text;
            return label === 'Booked' ? '#dc2626' : '#16a34a';
          }
        }
      }
    }
  }
  
});

  })
  </script>
  
  <style scoped>
  .dashboard {
    font-family: 'Segoe UI', sans-serif;
  }
  .dash {
    color: var(--text-primary);
  }
  
    .card-s {
        color: var(--text-primary);
    }
  .glass-card {
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.07);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    color: var(--text-primary);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
  }
  
  .glass-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    height: 4px;
    width: 100%;
    background: linear-gradient(to right, #6dd5ed, #2193b0);
  }
  
  .glass-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.298);
  }
  #pieChart {
  height: 305px;
  margin: 0 auto;
}
.bar-chart {
  height: 300px !important;
}
  </style>
  