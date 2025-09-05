<template>
    <form @submit.prevent="submitForm" class="add-lot-form container p-5">
      <h4 class="mb-4 fw-bold text-center">Edit Parking Lot</h4>
  
      <div class="row g-4">
        <div class="col-12">
          <input type="text" v-model="lot.prime_location" placeholder="Prime Location" required class="form-control form-control-lg" />
        </div>
        <div class="col-12">
          <input type="text" v-model="lot.address" placeholder="Address" required class="form-control form-control-lg" />
        </div>
        <div class="col-md-6">
          <input type="text" v-model="lot.pincode" placeholder="Pincode" required class="form-control form-control-lg" />
        </div>
        <div class="col-md-6">
          <input type="number" v-model="lot.price_per_hour" placeholder="Price per Hour" required class="form-control form-control-lg" />
        </div>
        <div class="col-12">
          <input type="number" v-model="lot.no_of_spots" placeholder="Number of Spots" disabled class="form-control form-control-lg" />
        </div>
      </div>
  
      <div class="d-flex justify-content-end gap-3 mt-5">
        <button type="submit" class="btn btn-success btn-lg px-4">Save</button>
        <button type="button" class="btn btn-outline-secondary btn-lg px-4" @click="emit('close')">Cancel</button>
      </div>
    </form>
  </template>
  
  <script setup>
  import { reactive, watch } from 'vue'
  const emit = defineEmits(['submit', 'close'])

  const props = defineProps({
  lotData: {
    type: Object,
    required: true
  }
})

  
  const lot = reactive({ ...props.lotData })
  
  watch(() => props.lotData, (newVal) => {
    Object.assign(lot, newVal)
  })
  
  const submitForm = () => {
    emit('submit', { ...lot })
  }
  </script>
  
  <style scoped>
  .add-lot-form {
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
  