<template>
  <div class="card shadow rounded-4 border-0 bg-glass p-4">
    <div class="card-body">
      <h5 class="card-title mb-4 fw-bold text-primary">Spot #{{ reservationDetails.spot_id }}</h5>

      <div v-if="reservationDetails.status === 'Occupied'">
        <ul class="list-group list-group-flush">
          <li class="list-group-item d-flex justify-content-between">
            <span class="fw-semibold">Status:</span>
            <span class="badge bg-danger">Occupied</span>
          </li>
          <li class="list-group-item d-flex justify-content-between">
            <span class="fw-semibold">User ID:</span>
            <span>{{ reservationDetails.user_id }}</span>
          </li>
          <li class="list-group-item d-flex justify-content-between">
            <span class="fw-semibold">Vehicle No.:</span>
            <span>{{ reservationDetails.vehicle_number }}</span>
          </li>
          <li class="list-group-item d-flex justify-content-between">
            <span class="fw-semibold">Parking Time:</span>
            <span>{{ reservationDetails.parking_time }}</span>
          </li>

          <li class="list-group-item d-flex justify-content-between">
            <span class="fw-semibold">Total Price:</span>
            <span class="text-success fw-bold">₹{{ totalPrice() }}</span>
          </li>
        </ul>
      </div>

      <div v-else class="text-center">
        <p class="fw-semibold text-success">Status: Available</p>
        <button class="btn btn-outline-danger rounded-pill px-4" @click="$emit('delete', reservationDetails.spot_id)">
          Delete Spot
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  reservationDetails: {
    type: Object,
    required: true,
  },
  lotDetails: Object
})

defineEmits(['delete'])

const totalPrice = () => {
  const { parking_time, current_time } = props.reservationDetails
  if (!parking_time || !current_time) return 0
  const start = new Date(parking_time)
  const end = new Date(current_time)
  const hours = Math.ceil((end - start) / (1000 * 60 * 60))
  return hours * props.lotDetails.price_per_hour
}
</script>

<style scoped>
.bg-glass {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(0, 0, 0, 0.05);
}
.card-title {
  border-bottom: 2px solid #0d6efd;
  padding-bottom: 0.5rem;
}
.list-group-item {
  background-color: transparent;
  border: none;
  padding: 0.6rem 0;
}
</style>
