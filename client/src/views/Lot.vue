<template>
    <div class="container py-4 change">
      <!-- Header -->
      <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h2 class="fw-bold mb-1">Parking Lots Management</h2>
          <p class="text-secondary">Manage your parking locations and settings</p>
        </div>
        <button class="btn btn-glow" @click="addLot()">
          <MapPinPlus class="me-1" /> Add New Lot
        </button>
      </div>
      <div class="search-bar card p-3 shadow-sm bg-white bg-opacity-10 mb-4 border-0">
  <div class="row g-2 align-items-center">
    <div class="col-md-3 d-flex align-items-center gap-2">
      <MapPin class="text-purple" />
      <input
        type="text"
        v-model="name"
        class="form-control form-control-sm  "
        placeholder="Search by Area Name"
      />
    </div>

    <div class="col-md-4 d-flex align-items-center gap-2">
      <MapPin class="text-purple" />
      <input
        type="text"
        v-model="address"
        class="form-control form-control-sm  "
        placeholder="Search by Address"
      />
    </div>

    <div class="col-md-3 d-flex align-items-center gap-2">
      <Flag class="text-purple" />
      <input
        type="number"
        v-model="pincode"
        class="form-control form-control-sm  "
        placeholder="Search by PIN code"
      />
    </div>

    <div class="col-md-2 d-flex justify-content-end">
      <button class="btn btn-glow w-100" @click="load_lots">
        <Search class="me-1" /> Filter
      </button>
    </div>
  </div>
</div>

      <!-- Lot Cards -->
      <div class="row g-4">
        <div v-for="lot in totalots" :key="lot.lot_id" class="col-md-6 col-lg-4">
          <div class="lot-card card h-100">
            <!-- View Spots -->
            <!-- <button class="btn btn-view-spots" @click="viewSpots(lot)">
              <LocationEdit class="me-1" /> View Spots
            </button> -->
  
            <div class="lot-card-content">
              <h5 class="fw-bold mb-2" style="color: var(--text-primary)">
                {{ lot.prime_location }}
              </h5>
  
              <!-- Badges -->
              <div class="d-flex align-items-center gap-2 mb-3">
                <span class="badge bg-success">{{ lot.spots.filter(s => s.status === true).length  }} Available</span>
                <span class="badge bg-secondary text-light">{{Math.round((lot.spots.filter(s => s.status === false).length / lot.no_of_spots) * 100)}}% Full</span>
              </div>
  
              <!-- Address -->
              <div class="d-flex align-items-center gap-2 small mb-2" style="color: var(--text-primary)">
                <MapPin class="text-purple" /> {{ lot.address }}
              </div>
  
              <!-- Row with PIN + Spots on left | Rate + Date on right -->
              <div class="d-flex justify-content-between flex-wrap mb-2">
                <!-- Left: PIN + Spots -->
                <div class="d-flex flex-column gap-1 small" style="color: var(--text-primary)">
                    <div class=" small" style="color: var(--text-primary)">PIN: <span class="fw-bold">{{ lot.pincode }}</span></div>
                <div class="d-flex align-items-center ">
                    <i class="bi bi-grid-3x3-gap-fill text-purple"></i> Total Spots:
                    <span class="fw-bold">{{ lot.no_of_spots }}</span>
                  </div>
                </div>
  
                <!-- Right: Rate + Date -->
                <div class="d-flex flex-column text-end gap-1 small">
                  <div class="text-success fw-bold d-flex align-items-center justify-content-end ">
                    <IndianRupee style="width: 14px; height: 14px"/>{{ lot.price_per_hour }}/hr
                  </div>
                  <div class="d-flex align-items-center justify-content-end gap-2" style="color: var(--text-primary)">
                    <i class="bi bi-calendar-event-fill text-purple"></i>{{ lot.date }}
                  </div>
                </div>
              </div>
  
              <!-- Buttons -->
              <div class="d-flex gap-2 mt-4">
                <button class="btn btn-view" @click="viewSpots(lot)">
                  <Eye class="me-1" /> View
                </button>
      
                <button class="btn btn-edit" @click="editingLot(lot)">
                  <SquarePen class="me-1" /> Edit
                </button>
                <button class="btn btn-delete" @click="deletingLot(lot.lot_id)">
                  <img src="@/assets/delete.svg" class="me-1"
                    style="width: 16px; height: 16px; object-fit: contain; margin-top: -2px; margin-right: 6px;" />
                  Delete
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Modal
        :is-open="showModal"
        @close="closeModal"
      >
      <AddLot v-if="addLotModal" @submit="handleLotSubmit" @close="closeModal"/>
      <EditLot 
        v-else-if="editLotModal"
        :lotData="selectedLotEdit"
        @submit="editLotSubmit"
        @close="closeModal"
        />
      <DeleteLot
        v-else-if="deleteLotModal"
        :lotId="selectedLotDelete"
        :delete-error="deleteError"
        @confirm="deleteCurrentLot"
        @cancel="closeModal"
      />
      <Spot
        v-else-if="selectedLot"
        :lot_id="selectedLot.lot_id"
        :no-of-spots="selectedLot.no_of_spots"
        :spots="selectedLot.spots"
        :area-name="selectedLot.prime_location"
        @refresh="load_lots"
      />
    </Modal>
      

  </template>

  <script setup>
  import { ref, onMounted } from 'vue'
  import Spot from '@/components/Spot.vue';
  import Modal from '@/components/Modal.vue'
  import AddLot from '@/components/AddLot.vue';
  import EditLot from '@/components/EditLot.vue';
  import DeleteLot from '@/components/DeleteLot.vue';
  import {
    Eye,
    LocationEdit,
    SquarePen,
    MapPinPlus,
    MapPin,
    IndianRupee,
    Flag
  } from 'lucide-vue-next'
  
  import { callApi, tokenChecker } from '@/utils.js'

  const totalots = ref([])
  const showModal = ref(false)
  const selectedLot = ref(null)
  const name = ref("")
  const address = ref("")
  const pincode = ref("")


  const load_lots = async () => {
  try {
    const { ok, status, resData } = await callApi(`lot?name=${name.value}&address=${address.value}&pincode=${pincode.value}`);
    if (ok) {
      totalots.value = resData;
      if (selectedLot.value) {
        const updated = resData.find(lot => lot.lot_id === selectedLot.value.lot_id)
        if (updated) {
          selectedLot.value = updated
        }
      }
    } else {
      alert(resData?.message || "Unauthorized")
      console.warn("Error fetching lots:", resData);
    }
  } catch (err) {
    console.error("Exception while loading lots:", err);
  }
};

  
  onMounted(load_lots)


const addLotModal = ref(false)
const editLotModal = ref(false)
const selectedLotEdit = ref(null)
const deleteLotModal = ref(false)
const selectedLotDelete =ref(null)
const deleteError = ref('')

function viewSpots(lot) {
  selectedLot.value = lot
  addLotModal.value = false
  showModal.value = true
}

function addLot(){
  addLotModal.value = true,
  showModal.value = true
}

function editingLot(lot){
  selectedLotEdit.value = lot
  editLotModal.value = true,
  showModal.value = true
}

function deletingLot(lot_id){
  selectedLotDelete.value = lot_id,
  deleteLotModal.value = true,
  showModal.value = true
}

const closeModal = () => {
      showModal.value = false
      selectedLot.value = null
      addLotModal.value = false
      editLotModal.value = false
      selectedLotEdit.value = null
      deleteLotModal.value = false
      selectedLotDelete.value = null
      deleteError.value = null
    }


    async function handleLotSubmit(lotData) {
  try {
    const { ok, status, resData } = await callApi('lot', 'POST', lotData)

    if (ok) {
      await load_lots()
      closeModal()
    } else {
      alert(resData?.message || `Failed to add lot (Status: ${status})`)
    }
  } catch (err) {
    alert("Unexpected error while adding lot.")
    console.error(err)
  }
}

  async function editLotSubmit(lotDetail) {
  try {
    const { ok, status, resData } = await callApi(`lot/${lotDetail.lot_id}`, 'PUT', lotDetail)

    if (ok) {
      await load_lots()
      closeModal()
    } else {
      alert(resData?.message || `Failed to edit lot (Status: ${status})`)
    }
  } catch (err) {
    alert("Unexpected error while editing lot.")
    console.error(err)
  }
}
  async function deleteCurrentLot(lot_id) {
  try {
    const { ok, status, resData } = await callApi(`lot/${lot_id}`, 'DELETE')

    if (ok) {
      await load_lots()
      closeModal()
    } else {
      deleteError.value = resData?.message || `Failed to delete lot (Status: ${status})`
      

    }
  } catch (err) {
    deleteError.value = "Unexpected error while trying to delete the lot."
    console.error(err)
  }
}


  </script>
  
  <style scoped>
  .change {
    color: var(--text-primary);
  }
  
  .card.lot-card {
    background: transparent;
    backdrop-filter: blur(12px);
    border-radius: 1rem;
    border: 1px solid rgba(255, 255, 255, 0.08);
    position: relative;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
    padding-top: 1.5rem;
    transition: all 0.3s ease;
  }
  
  .lot-card-content {
    padding: 1.5rem;
    position: relative;
    z-index: 2;
  }
  
  /* View Spots button */
  .btn-view-spots {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: transparent;
    color: #FFB6C1;
    border: 1px solid #FFB6C1;
    padding: 4px 12px;
    font-size: 13px;
    font-weight: 500;
    transition: all 0.2s ease;
    z-index: 3;
  }
  
  .btn-view-spots:hover {
    background-color: #ff9fb271;
  }
  
  /* Gradient Top Border */
  .card.lot-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 4px;
    width: 100%;
    background: #B0E0E6;
    border-top-left-radius: 1rem;
    border-top-right-radius: 1rem;
    z-index: 1;
  }
  
  /* Buttons */
  .btn-view {
    color: #9333ea;
    border-color: #5932be;
    font-weight: 500;
    padding: 6px 16px;
    transition: all 0.3s ease;
  }
  
  .btn-view:hover {
    background-color: #5c3ca83b;
  }
  
  .btn-edit {
    color: #6c757d;
    border-color: #6c757d;
    padding: 6px 16px;
    font-weight: 500;
  }
  
  .btn-edit:hover {
    background-color: #5a626863;
  }
  
  .btn-delete {
    color: rgb(230, 14, 14);
    border-color: #c82333;
    padding: 6px 16px;
    font-weight: 500;
  }
  
  .btn-delete:hover {
    background-color: #ee3a4f1e;
  }
  
  .btn-glow {
    background-color: #14B8A6;
    color: #0f172a;
    font-weight: 500;
    border: none;
    padding: 8px 20px;
    transition: all 0.3s ease;
  }
  
  .btn-glow:hover {
    background-color: #2dd4bf;
    box-shadow: 0 0 16px #14B8A6;
  }
  
  .text-purple {
    color: #a78bfa;
  }
  </style>
  