<template>
    <div class="container p-3">
      <h4 class="modal-title fw-bold">Logout</h4>
      <div>
        <p >Are you sure you want to Logout?</p>
      </div>
      <div class="d-flex justify-content-end gap-3 mt-3">
        <button class="btn btn-secondary" @click="$emit('cancel')">Cancel</button>
        <button class="btn btn-danger" @click="$emit('confirm')">Confirm</button>
      </div>
    </div>
  </template>
  
  <script setup>
  defineEmits(['confirm', 'cancel'])
  </script>
  