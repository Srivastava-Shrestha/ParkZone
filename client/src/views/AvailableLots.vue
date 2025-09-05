<template>
    <div class="app">
      <div class="page-container">

        <!--Current Bookings -->
        <div class="section">
          <h3 class="section-title"> Current Bookings</h3>
          <div class="table-wrapper">
            <table class="table custom-table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Prime Location</th>
                  <th>Address</th>
                  <th>Vehicle Number</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(reservation, index) in currentBookings" :key="reservation.reservation_id">
                  <td>{{ index + 1 }}</td>
                  <td>{{ reservation.prime_location }}</td>
                  <td>{{ reservation.address }}</td>
                  <td>{{ reservation.vehicle_number }}</td>
                  <td>
                    <button
                      class="btn btn-status" @click="handleReservation(reservation)"
                      :class="statusClass(reservation.parking_time)"
                    >
                      {{ reservation.parking_time ? 'Release' : 'Occupy' }}
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
  
        <!--Available Parking Lots -->
        <div class="section">
          <h3 class="section-title"> Available Parking Lots</h3>
          <div class="table-wrapper">
            <table class="table custom-table">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Prime Location</th>
                  <th>Address</th>
                  <th>Total Spots</th>
                  <th>Available</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(lot, index) in parkingLots" :key="lot.lot_id">
                  <td>{{ index + 1 }}</td>
                  <td>{{ lot.prime_location }}</td>
                  <td>{{ lot.address }}</td>
                  <td>{{ lot.no_of_spots }}</td>
                  <td>{{ lot.spots.filter(s => s.status === true).length }}</td>
                  <td>
                    <button
                      class="btn btn-pastel-blue" @click="viewBook(lot)"> Book
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <Modal
      :is-open="showModal"
      @close="closeModal"
    >
      <BookSpot v-if="!isReleasePay"
      :lot=selectedLot
      @cancel="closeModal"
      >

      </BookSpot>
      <Release v-else
      :reservationDetail=order
      @cancel="closeModal"
      >

      </Release>
    </Modal>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { callApi } from '@/utils.js'
  import BookSpot from '@/components/BookSpot.vue'
  import Modal from '@/components/Modal.vue'
  import Release from '@/components/Release.vue'
  
  const currentBookings = ref([])
  
  const parkingLots = ref([])
  
  const showModal = ref(false)

  const selectedLot = ref()

  const isReleasePay = ref(false)


  const getParkingLot = async () => {
    try {
      const { ok, status, resData } = await callApi('lot');
      if (ok) {
        parkingLots.value = resData;
      } else {
        alert(resData?.message || "Unauthorized")
        console.warn("Error fetching lots:", resData);
      }
    } catch (err) {
      console.error("Exception while loading lots:", err);
    }
    
  }


  const currentBooking = async () => {
    try {
      const { ok, status, resData } = await callApi('reservation');
    if (ok) {
      currentBookings.value = resData;
    } else {
      alert(resData?.message || "Unauthorized")
      console.warn("Error fetching reservations:", resData)
    }
    } catch (err) {
      console.error("Exception while loading lots:", err)
    }
  }
  onMounted(() => {
  getParkingLot()
  currentBooking()
  
})
const handleReservation = async (reservation) => {
  if (reservation.parking_time) {
    await releaseSpot(reservation.reservation_id)
    isReleasePay.value = true
    showModal.value = true
  } else {
    await occupySpot(reservation.reservation_id)
  }
}


  
  const statusClass = (status) => {
    if (!status) {
      return 'btn btn-pastel-yellow'
    } else {
      return 'btn btn-pastel-red'
    }
}

  function viewBook (lot) {
    selectedLot.value = lot
    showModal.value=true
  }

  const occupySpot = async (id) => {
    try{
      const {ok, status, resData} = await callApi(`reservation/${id}`, "PUT", {"parked": true})
      if (ok) {
        currentBooking()
      }
    } catch (err) {
      alert("Something went wrong!")
      console.log(err)
    }
  }

  const order = ref({})

const releaseSpot = async (id) => {
  try {
    const { ok, resData } = await callApi(`payment?reservation_id=${id}`)
    if (ok) {
      order.value = resData
    }
  } catch (err) {
    console.log(err)
  }
}


//  const releaseSpot = async (id) => {
//   try{
//     const {ok, status, resData} = await callApi(`payment?reservation_id=${id}`)
//     if (ok) {
//       order.value = resData
//       const options = {
//         key: import.meta.env.VITE_RAZORPAY_CLIENT_ID,
//         amount: order.value.amount,
//         currency: order.value.currency,
//         name: "ParkZone",
//         description: "Reservation Fee",
//         order_id: order.value.id,
//         handler: async (response) => {
                
//             },
//             theme: {
//                 color: 'rgba(94, 234, 212, 0.5)',
//             },
//         };

//         const rzp1 = new Razorpay(options);
//         rzp1.open(); 
//       }
//     } catch (err) {
//       console.log(err)
//     }
//  }





  const closeModal = () => {
    showModal.value = false
    selectedLot.value = null
    currentBooking()
    getParkingLot()
    isReleasePay.value=false

 }

 
 

  </script>
  
  <style scoped>
  .app {
    background-color: var(--bg-primary);
    min-height: 100vh;
    color: var(--text-primary);
    font-family: 'Segoe UI', sans-serif;
  }
  
  .page-container {
    padding: 3rem 2rem 2rem 2.5rem;
  }
  
  .section {
    margin-bottom: 3rem;
  }
  
  .section-title {
    font-size: 1.9rem;
    font-weight: 700;
    margin-bottom: 1.4rem;
    color: var(--text-primary);
    padding-left: 0.8rem;
  }
  
  .table-wrapper {
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
    background: rgba(255, 255, 255, 0.02);
  }
  
  .custom-table {
    margin: 0;
    width: 100%;
    border-collapse: collapse;
  }
  
  .custom-table thead {
    background: rgba(255, 255, 255, 0.06);
  }
  
  .custom-table th,
  .custom-table td {
    background-color: var(--bg-secondary);
    color: var(--text-primary);
    vertical-align: middle;
    text-align: center;
    padding: 1rem 0.8rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.07);
    transition: background 0.3s ease;
  }
  
  .custom-table tbody tr:hover td {
    background-color: rgba(255, 255, 255, 0.07);
  }
  
  .btn-status {
    min-width: 90px;
    font-weight: 600;
    border-radius: 10px;
    padding: 6px 14px;
    font-size: 0.85rem;
    transition: 0.2s ease;
  }
  .btn {
  border: none;
  font-weight: 600;
  border-radius: 10px;
  padding: 8px 18px;
  font-size: 0.9rem;
  transition: all 0.2s ease-in-out;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
}

.btn-status {
  min-width: 90px;
}

/* Book - Pastel Blue */
.btn-pastel-blue {
  background-color: #c2e9fb;
  color: #124b77;
}
.btn-pastel-blue:hover {
  background-color: #b1dbf1;
  transform: scale(1.05);
}

/* Occupy - Pastel Yellow */
.btn-pastel-yellow {
  background-color: #fff7c2;
  color: #7a5e00;
}
.btn-pastel-yellow:hover {
  background-color: #ffee99;
  transform: scale(1.05);
}

/* Release - Pastel Red */
.btn-pastel-red {
  background-color: #fddede;
  color: #892828;
}
.btn-pastel-red:hover {
  background-color: #fbc4c4;
  transform: scale(1.05);
}

/* Parked Out - Pastel Grey */
.btn-pastel-grey {
  background-color: #e4e4e4;
  color: #4a4a4a;
}
.btn-pastel-grey:hover {
  background-color: #d4d4d4;
  transform: scale(1.05);
}

  </style>
  