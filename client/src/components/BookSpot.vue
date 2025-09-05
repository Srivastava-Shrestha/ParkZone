<template>
    <form @submit.prevent="reserve" class="book-lot-form container p-5">
      <h4 class="mb-4 fw-bold text-center">Book Parking Spot</h4>
  
      <div class="row g-4">
        <div class="col-12 d-flex align-items-center">
          <label class="me-3 fw-bold" style="min-width: 120px;">Spot ID: </label>
          <input type="text" v-model="spot_id" placeholder="Spot Id" disabled class="form-control form-control-lg" />
        </div>
        <div class="col-12 d-flex align-items-center">
          <label class="me-3 fw-bold" style="min-width: 120px;">Lot ID: </label>
          <input type="text" v-model="lot.lot_id" placeholder="Lot Id" disabled class="form-control form-control-lg" />
        </div>
        <div class="col-md-12 d-flex align-items-center">
          <label class="me-3 fw-bold" style="min-width: 120px;">User Id: </label>
          <input type="text" v-model="store.id" placeholder="User Id" disabled class="form-control form-control-lg" />
        </div>
        <div class="col-12 d-flex align-items-center">
          <label class="me-3 fw-bold" style="min-width: 120px;">Price Per Hour: </label>
          <input type="number" v-model="lot.price_per_hour" placeholder="Price Per Hour" disabled class="form-control form-control-lg" />
        </div>
        <div class="col-md-12 d-flex align-items-center">
          <label class=" fw-bold" style="min-width: 130px;">Vehicle Number:</label>
          <input type="text" v-model="vehicle_number" placeholder="Vehicle Number" required class="form-control form-control-lg" />
        </div>
        
      </div>
  
      <div class="d-flex justify-content-end gap-3 mt-5">
        <button type="submit" class="btn btn-success btn-lg px-4">Reserve</button>
        <button type="button" class="btn btn-outline-secondary btn-lg px-4" @click="emit('cancel')">Cancel</button>
      </div>
    </form>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue'
  import { dataStore } from '@/store/data.js'
  import { callApi } from '@/utils.js'

  const store = dataStore()
  

  const emit = defineEmits(['cancel'])

  const props = defineProps({
  lot: {
    type: Object,
    required: true
  }
})

const spot_id = ref()
const vehicle_number = ref()

function randomSpot(lot) {
  for (const spot of lot.spots) {
    if (spot.status === true) {
      spot_id.value = spot.spot_id;
      break; 
    }
  }
}

onMounted(() => randomSpot(props.lot))

const reserve = async () => {
    try {
        const payload = {
            "vehicle_number": vehicle_number.value
        }
        const { ok, status, resData} = await callApi(`reservation/spot/${spot_id.value}`, 'POST', payload);
        if (ok) {
            emit('cancel')
        }
    } catch (err) {
        alert('Reservation not Done!')
        console.log(err)
    }
}

  </script>
  
  <style scoped>
  .book-lot-form {
    background: var(--bg-modalbg);
    border-radius: 1rem;
    max-width: 720px;
    width: 100%;
  }
  input::placeholder {
    font-weight: 500;
    color: #6c757d;
  }
  input:focus {
    box-shadow: 0 0 0 0.2rem rgba(25, 135, 84, 0.25);
  }
  </style>
  