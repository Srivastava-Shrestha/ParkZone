<template>
    <div class="dashboard custom-container py-4">
      <div class="d-flex justify-content-between align-items-center mb-4">
        <h2 class="fw-bold dash m-0 d-flex align-items-center">
            Parking Insights <ArrowBigRightDash class="ms-2" />
        </h2>
      <button class="btn btn-glow" @click="export_csv()">
        <FileDown class="me-1" /> CSV Export
        </button>
      </div>
    </div>
      <!-- Info Cards -->
      <div class="row g-4 mb-4 custom-container">
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
      <div class="row g-4 custom-container" >
        <div class="col-md-6">
          <div class="card glass-card p-4">
            <h6 class="fw-semibold mb-3">Monthly Reservation Distribution</h6>
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
  </template>
  
  <script setup>
  import { onMounted, reactive, ref, computed } from 'vue'
  import { ParkingSquare, Bookmark, Zap, FileDown, IndianRupee, ArrowBigRightDash } from 'lucide-vue-next'
  import Chart from 'chart.js/auto'
  import {callApi} from '@/utils.js'


  const cardDetails = ref({})
  const cardss = async () => {
    try {
      const {ok, status, resData } = await callApi('stats')
      if (ok) {
        cardDetails.value = resData
      } else {
        alert(resData?.message || "No Lots fetch!")
      }
    } catch (err) {
      console.log(err)
    }
  }

  
  const cards = computed(() => [
  { label: 'Total Reservations', value: cardDetails.value.total_reservations, icon: ParkingSquare, color: '#3b82f6' },
  { label: 'Total Bookings', value:cardDetails.value.total_bookings, icon: Bookmark, color: '#f59e0b' },
    { label: 'Total Amount Spent', value:`₹ ${cardDetails.value.total_amount}`, icon: IndianRupee, color: '#22c55e' },
    { label: 'Most Visited Lot', value: cardDetails.value.most_visited_lot, icon: Zap, color: '#ef4444' },
  ])
  
  const export_csv = async () => {
    try {
      const {ok, status, resData } = await callApi('export')
      if (ok) {
        alert(resData.message)
      } else {
        alert(resData?.message || "No Lots fetch!")
      }
    } catch (err) {
      console.log(err)
    }
  } 


  onMounted( async() => {
    await cardss();
    new Chart(document.getElementById('barChart'), {
  type: 'bar',
  data: {
    labels:Object.keys(cardDetails.value.barchart),
    datasets: [
      {
        label: 'Reservations',
        data: Object.values(cardDetails.value.barchart),
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
    layout: {
  padding: {
    left: 0,
    right: 0
  }
},
    plugins: {
      legend: { display: false },
      labels: {
        color: '#64748b'},
      title: {
        display: true,
        text: 'Reservations per Month',
        color:"#64748b",
        font: { size: 16, weight: 'bold' }
      }
    },
    scales: {
    x: {
      title: {
        display: true,
        text: 'Months',
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
    labels: Object.keys(cardDetails.value.piechart),
    datasets: [{
      data: Object.values(cardDetails.value.piechart),
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
  .btn-glow {
    background-color: #14B8A6;
    color: #0f172a;
    font-weight: 500;
    border: none;
    padding: 8px 20px;
    transition: all 0.3s ease;
  }
  .custom-container {
  padding-left: 1.8rem;
  padding-right: 1.8rem;
}

@media (min-width: 1400px) {
  .custom-container {
    padding-left: 3.5rem;
    padding-right: 3.5rem;
  }
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
  