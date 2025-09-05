<template>
  <div class="container p-3">
    <h5 class="modal-title">Confirm Deletion</h5>
    <div>
      <p v-if="!deleteError">Are you sure you want to delete this lot?</p>
      <p v-if="deleteError" class="text-danger mt-2 mb-0 text-center">
        {{ deleteError }}
      </p>
    </div>
    <div class="d-flex justify-content-end gap-3 mt-3">
      <button class="btn btn-secondary" @click="$emit('cancel')">Cancel</button>
      <button class="btn btn-danger" @click="$emit('confirm', lotId)">Delete</button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  lotId: Number,
  deleteError: String
})
defineEmits(['confirm', 'cancel'])
</script>
