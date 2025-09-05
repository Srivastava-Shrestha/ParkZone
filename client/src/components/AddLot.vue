<template>
    <form @submit.prevent="submitForm" class="add-lot-form container p-5">
      <h4 class="mb-4 fw-bold text-center">Add New Parking Lot</h4>
  
      <div class="row g-4">
        <div class="col-12">
          <input type="text" v-model="newLot.prime_location" placeholder="Prime Location" required class="form-control form-control-lg" />
        </div>
        <div class="col-12">
          <input type="text" v-model="newLot.address" placeholder="Address" required class="form-control form-control-lg" />
        </div>
        <div class="col-md-6">
          <input type="text" v-model="newLot.pincode" placeholder="Pincode" required class="form-control form-control-lg" />
        </div>
        <div class="col-md-6">
          <input type="number" v-model="newLot.price_per_hour" placeholder="Price per Hour" required class="form-control form-control-lg" />
        </div>
        <div class="col-12">
          <input type="number" v-model="newLot.no_of_spots" placeholder="Number of Spots" required class="form-control form-control-lg" />
        </div>
      </div>
  
      <div class="d-flex justify-content-end gap-3 mt-5">
        <button type="submit" class="btn btn-success btn-lg px-4">Add Lot</button>
        <button type="button" class="btn btn-outline-secondary btn-lg px-4" @click="emit('close')">Cancel</button>
      </div>
    </form>
  </template>
  
  <script setup>
  import { reactive } from 'vue'
  const emit = defineEmits(['submit', 'close'])
  
  const newLot = reactive({
    prime_location: '',
    address: '',
    pincode: '',
    price_per_hour: null,
    no_of_spots: null,
  })
  
  const submitForm = () => {
    emit('submit', { ...newLot })
  }
  </script>
  
  <style scoped>
  .add-lot-form {
    background: var(--bg-modalbg);
    border-radius: 1rem;
    /* box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15); */
    max-width: 720px;
    width: 100%;
  }
  
  input::placeholder {
    font-weight: 500;
    color: #6c757d;
  }
  
  input:focus {
    box-shadow: 0 0 0 0.2rem rgba(25, 135, 84, 0.25); /* green glow */
  }
  </style>
  