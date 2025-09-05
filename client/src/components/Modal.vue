<template>
    <div v-if="isOpen" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop >
        <!-- Close button -->
        <button class="close-button" @click="closeModal">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
  
        <!-- Modal content slot -->
        <slot></slot>
      </div>
    </div>
  </template>
  
  <script setup>  
  // Props
  defineProps({
    isOpen: {
      type: Boolean,
      default: false
    }
  })
  
  // Emits
  const emit = defineEmits(['close'])
  
  // Close function
  const closeModal = () => {
    emit('close')
  }
  
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    padding: 20px;
    backdrop-filter: blur(4px);
  }
  
  .modal-content {
    position: relative;
    max-width: 800px;
    width: 100%;
    max-height: 90vh;
    color: var(--text-modal);
    overflow-y: auto;
    background: var(--bg-modalbg);
    border-radius: 16px;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    animation: modalSlideIn 0.3s ease-out;
  }
  
  .close-button {
    position: absolute;
    top: 16px;
    right: 16px;
    background: var(--bg-modalbg);
    border: none;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 10;
    transition: all 0.2s ease;
    color: #666;
  }
  
  .close-button:hover {
    background: rgba(255, 255, 255, 1);
    color: #333;
    transform: scale(1.05);
  }
  
  @keyframes modalSlideIn {
    from {
      opacity: 0;
      transform: scale(0.95) translateY(-20px);
    }
    to {
      opacity: 1;
      transform: scale(1) translateY(0);
    }
  }
  
  @media (max-width: 768px) {
    .modal-overlay {
      padding: 10px;
    }
  
    .modal-content {
      max-height: 95vh;
      border-radius: 12px;
    }
  
    .close-button {
      top: 12px;
      right: 12px;
      width: 36px;
      height: 36px;
    }
  }
  </style>
  