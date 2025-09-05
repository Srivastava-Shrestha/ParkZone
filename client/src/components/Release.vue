<template>
    <form @submit.prevent="payNow" class="book-lot-form container p-5">
      <h4 class="mb-4 fw-bold text-center">Book Parking Spot</h4>
  
      <div class="row g-4">
        <div class="col-12 d-flex align-items-center">
            <label class="me-3 fw-bold" style="min-width: 120px;">Spot ID:</label>
            <input type="text" v-model="details.spot_id" disabled class="form-control form-control-lg" />
        </div>
        <div class="col-12 d-flex align-items-center">
            <label class="me-3 fw-bold" style="min-width: 120px;">Vehicle Number:</label>
            <input type="text" v-model="details.vehicle_number" disabled class="form-control form-control-lg" />
        </div>
        <div class="col-12 d-flex align-items-center">
            <label class="me-3 fw-bold" style="min-width: 120px;">Parking Time:</label>
            <input type="text" v-model="details.parking_time" disabled class="form-control form-control-lg" />
        </div>
        <div class="col-12 d-flex align-items-center">
            <label class="me-3 fw-bold" style="min-width: 120px;">Leaving Time:</label>
            <input type="text" v-model="details.leaving_time" disabled class="form-control form-control-lg" />
        </div>
        <div class="col-12 d-flex align-items-center">
            <label class="me-3 fw-bold" style="min-width: 120px;">Total Cost:</label>
            <input type="text" :value=details.total_cost/100 disabled class="form-control form-control-lg" />
        </div>
    </div>

        
    
  
      <div class="d-flex justify-content-end gap-3 mt-5">
        <button type="submit" class="btn btn-success btn-lg px-4">Pay & Release</button>
        <button type="button" class="btn btn-outline-secondary btn-lg px-4" @click="emit('cancel')">Cancel</button>
      </div>
    </form>
  </template>
  
  <script setup>
  import { onMounted, ref, watchEffect} from 'vue'
  import { dataStore } from '@/store/data.js'
  import { callApi } from '@/utils.js'
  import { useRouter } from 'vue-router'

  const store = dataStore()
  const router = useRouter()

  const emit = defineEmits(['cancel'])

  const props = defineProps({
  reservationDetail: {
    type: Object,
    required: true
  }
})
const details = ref({})

watchEffect(() => {
  details.value = props.reservationDetail.reservation_data
})
const order = props.reservationDetail.order

const payNow = () => {
  const options = {
    key: import.meta.env.VITE_RAZORPAY_CLIENT_ID,
    amount: order.amount,
    currency: order.currency,
    name: "ParkZone",
    description: "Reservation Fee",
    order_id: order.id,
    handler: async (response) => {
      try {
        const payload = {
          "reservation_id":details.value.reservation_id,
          "order_id": response.razorpay_order_id,
          "payment_id": response.razorpay_payment_id,
          "signature": response.razorpay_signature,
          "total_cost":details.value.total_cost,
          "amount": order.amount
        }
        const {ok, status, resData } = await callApi("payment", "POST", payload)
        if (ok) {
          emit('cancel')
          router.push('/dashboard/parking-history')

        } else {
          alert("Something went wrong")
        }
      } catch {
          console.error(err)
          alert('Verification failed!');
      }
    },
    theme: { color: 'rgba(94, 234, 212, 0.5)' },
  }

  const rzp = new Razorpay(options)
  rzp.open()
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
  