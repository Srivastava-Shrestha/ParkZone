<template>
    <div class="parking-container">
      <!-- Header Section -->
      <div class="header">
        <div class="header-content">
          <h1 class="title">{{ areaName || 'Downtown Central Parking' }}</h1>
          <p class="subtitle">Grid view of all spots</p>
        </div>
      </div>
  
      <!-- Parking Grid -->
      <div class="parking-grid" :style="{ gridTemplateColumns: 'repeat(4, 1fr)' }">
        <div
          v-for="(spot,index) in props.spots" :key='index'
          class="parking-spot"
          :class="{ 'available': spot.status, 'occupied': !spot.status }"
          @click="viewSpotDetail(spot)"
        >
          <!-- Car Icon -->
          <div class="car-icon">
            <svg viewBox="0 0 24 24" width="16" height="16">
              <path
                d="M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.22.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.5 16c-.83 0-1.5-.67-1.5-1.5S5.67 13 6.5 13s1.5.67 1.5 1.5S7.33 16 6.5 16zm11 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM5 11l1.5-4.5h11L19 11H5z"
                fill="currentColor"
              />
            </svg>
          </div>
          <!-- Spot Number -->
          <div class="spot-number">{{ index+1 }}</div>
        </div>
      </div>
  
      <div class="status-indicators">
        <div class="status-item available">
          <div class="status-dot available-dot"></div>
          <span>Available: {{ availableCount }}</span>
        </div>
        <div class="status-item occupied">
          <div class="status-dot occupied-dot"></div>
          <span>Occupied: {{ occupiedCount }}</span>
        </div>
      </div>
    </div>

    <Modal
      :is-open="showModal"
      @close="closeModal"
    >
    <SpotDetail
      :reservationDetails="reservationDetails" :lotDetails="lotDetails" @delete="deleteSpot">
    </SpotDetail>

    </Modal>
  </template>
  
  <script setup>
  import { computed, ref } from 'vue'
  import Modal from '@/components/Modal.vue'
  import SpotDetail from '@/components/SpotDetail.vue'
  import { callApi } from '@/utils.js'

  const props = defineProps({
    noOfSpots: {
      type: Number,
      required: true
    },
    spots: {
      type: Array,
      required: true
    },
    areaName: {
      type: String,
      default: 'Downtown Central Parking'
    },
    lot_id: Number,
    required:true
  })
  



  const emit = defineEmits(['refresh'])
  
  const availableCount = computed(() =>
    props.spots.filter(spot => spot.status).length
  )
  
  const occupiedCount = computed(() =>
    props.spots.filter(spot => !spot.status).length
  )
  

  const showModal = ref(false)
  const reservationDetails = ref()


  const viewSpotDetail = async (spot) => {
    const {ok, status, resData } = await callApi(`reservation/spot/${spot.spot_id}`)
    if (ok) {
      reservationDetails.value = resData
      await fetchLotDetails()
    } 
    showModal.value = true
  
  }

  const deleteSpot = async (spot_id) => {
    try {
    const { ok, status, resData } = await callApi(`spot/${spot_id}`, 'DELETE')
    if (ok) {
      emit('refresh')
      closeModal()
    } else {
      alert(resData?.message || `Failed to delete lot (Status: ${status})`)
      

    }
  } catch (err) {
    alert("Unexpected error while trying to delete the lot.")
    console.error(err)
  }
  }

  const closeModal = () => {
    showModal.value = false
    reservationDetails.value = null
     

  }
  const lotDetails = ref(null)

const fetchLotDetails = async () => {
  try {
    const { ok, resData } = await callApi(`lot/${props.lot_id}`)
    if (ok) {
      lotDetails.value = resData
    } else {
      console.warn("Could not fetch lot details.")
    }
  } catch (err) {
    console.error("Error loading lot details:", err)
  }
}

//   const gridStyle = computed(() => {
//     const columns = Math.ceil(Math.sqrt(props.noOfSpots))
//     return {
//       gridTemplateColumns: `repeat(${Math.min(columns, 10)}, 1fr)`
//     }
//   })
  </script>
  
  <style scoped>
  /* [no changes in CSS — same as you provided] */
  .parking-container {
    width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f5f5f5;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid #e0e0e0;
  }
  
  .header-content {
    flex: 1;
  }
  
  .title {
    font-size: 24px;
    font-weight: 600;
    color: #333;
    margin: 0 0 4px 0;
  }
  
  .subtitle {
    font-size: 14px;
    color: #666;
    margin: 0;
  }
  
  .status-indicators {
    display: flex;
    gap: 16px;
    align-items: center;
  }
  
  .status-item {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 14px;
    font-weight: 500;
  }
  
  .status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
  }
  
  .available-dot {
    background-color: #4ade80;
  }
  
  .occupied-dot {
    background-color: #f87171;
  }
  
  .available {
    color: #059669;
  }
  
  .occupied {
    color: #dc2626;
  }
  
  .parking-grid {
    display: grid;
    gap: 8px;
    padding: 16px;
    background-color: white;
    border-radius: 8px;
  }
  
  .parking-spot {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 12px 8px;
    border-radius: 8px;
    transition: all 0.2s ease;
    cursor: pointer;
    min-height: 60px;
    border: 2px solid transparent;
    position: relative;
  }
  
  .parking-spot:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }
  
  .parking-spot.available {
    background-color: #dcfce7;
    border-color: #4ade80;
  }
  
  .parking-spot.available:hover {
    background-color: #bbf7d0;
  }
  
  .parking-spot.occupied {
    background-color: #fecaca;
    border-color: #f87171;
  }
  
  .parking-spot.occupied:hover {
    background-color: #fca5a5;
  }
  
  .car-icon {
    color: currentColor;
    margin-bottom: 4px;
    opacity: 0.8;
  }
  
  .spot-number {
    font-size: 14px;
    font-weight: 600;
    color: currentColor;
  }
  
  /* Responsive Design */
  @media (max-width: 768px) {
    .parking-container {
      padding: 16px;
    }
  
    .header {
      flex-direction: column;
      gap: 12px;
      align-items: flex-start;
    }
  
    .status-indicators {
      gap: 12px;
    }
  
    .parking-grid {
      grid-template-columns: repeat(auto-fit, minmax(60px, 1fr)) !important;
      gap: 6px;
      padding: 12px;
    }
  
    .parking-spot {
      min-height: 50px;
      padding: 8px 4px;
    }
  
    .title {
      font-size: 20px;
    }
  }
  
  @media (max-width: 480px) {
    .parking-grid {
      grid-template-columns: repeat(auto-fit, minmax(50px, 1fr)) !important;
    }
  
    .parking-spot {
      min-height: 45px;
      padding: 6px 2px;
    }
  
    .spot-number {
      font-size: 12px;
    }
  }
  </style>
  