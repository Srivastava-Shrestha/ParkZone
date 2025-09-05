<template>
  <div class="screen">

    <!-- Signup Section -->
    <section class="login-section">
      <div class="login-container glossy-card">
        <div class="row align-items-stretch g-0">
          <!-- Left Art -->
          <div class="col-lg-6">
            <div class="art-wrap">
              <img class="art-img floaty" src="/src/assets/login.png" alt="mascot illustration" />
            </div>
          </div>

          <!-- Right Form -->
          <div class="col-lg-6 form-column">
            <div class="form-wrap">
              <h2 class="login-title">Sign Up to ParkZone</h2>

              <form @submit.prevent="step === 1 ? nextStep() : signup()">
                <!-- Step 1: Credentials -->
                <div v-if="step === 1">
                  <div class="mb-3">
                    <label class="form-label">Username</label>
                    <div class="input-shell">
                      <span class="left-ico">
                        <!-- User Icon -->
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                          <circle cx="12" cy="6" r="4" stroke="#fff" stroke-width="1.7" />
                          <path d="M15 20.615C14.0907 20.8619 13.0736 21 12 21c-1.0736 0-2.0907-.1381-3-.3849M14 21v-5.5c0-1.1046-.8954-2-2-2s-2 .8954-2 2V21" stroke="#fff" stroke-width="1.7" />
                        </svg>
                      </span>
                      <input v-model="username" type="text" class="form-control" placeholder="Enter username" required />
                    </div>
                  </div>

                  <div class="mb-3">
                    <label class="form-label">Email</label>
                    <div class="input-shell">
                      <span class="left-ico">
                        <!-- Mail Icon -->
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                          <path
                            d="M4 6h16a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1z"
                            stroke="#fff"
                            stroke-width="1.7"
                          />
                          <path d="M5 7l7 6 7-6" stroke="#fff" stroke-width="1.7" fill="none" />
                        </svg>
                      </span>
                      <input v-model="email" type="email" class="form-control" placeholder="Enter email" required />
                    </div>
                  </div>

                  <div class="mb-3">
                    <label class="form-label">Password</label>
                    <div class="input-shell">
                      <span class="left-ico">
                        <!-- Lock Icon -->
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                          <rect
                            x="4"
                            y="11"
                            width="16"
                            height="9"
                            rx="2.2"
                            stroke="#fff"
                            stroke-width="1.7"
                          />
                          <path
                            d="M8 11V8a4 4 0 1 1 8 0v3"
                            stroke="#fff"
                            stroke-width="1.7"
                          />
                        </svg>
                      </span>
                      <input :type="showPwd ? 'text' : 'password'" v-model="password" class="form-control pe-5" placeholder="Password" required />
                      <button type="button" class="btn position-absolute end-0 top-0 h-100 px-3 border-0 bg-transparent" @click="showPwd = !showPwd" aria-label="Toggle password">
                        <svg
                          v-if="!showPwd"
                          width="20"
                          height="20"
                          viewBox="0 0 24 24"
                          fill="none"
                        >
                          <path
                            d="M2.5 12s3.7-6.5 9.5-6.5S21.5 12 21.5 12 17.8 18.5 12 18.5 2.5 12 2.5 12z"
                            stroke="#fff"
                            stroke-width="1.7"
                          />
                          <circle
                            cx="12"
                            cy="12"
                            r="3"
                            stroke="#fff"
                            stroke-width="1.7"
                          />
                        </svg>
                        <svg
                          v-else
                          width="20"
                          height="20"
                          viewBox="0 0 24 24"
                          fill="none"
                        >
                          <path d="M3 3l18 18" stroke="#fff" stroke-width="1.7" />
                          <path
                            d="M6 6.8C3.8 8.4 2.5 12 2.5 12s3.7 6.5 9.5 6.5c1.6 0 3-.3 4.2-.8M16.5 8.2C15.2 7.6 13.7 7.5 12 7.5 6.2 7.5 2.5 12 2.5 12"
                            stroke="#fff"
                            stroke-width="1.7"
                          />
                        </svg>
                      </button>
                    </div>
                  </div>

                  <div class="mb-3">
                    <label class="form-label">Confirm Password</label>
                    <div class="input-shell">
                      <span class="left-ico">
                        <!-- Lock Icon -->
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                          <rect
                            x="4"
                            y="11"
                            width="16"
                            height="9"
                            rx="2.2"
                            stroke="#fff"
                            stroke-width="1.7"
                          />
                          <path
                            d="M8 11V8a4 4 0 1 1 8 0v3"
                            stroke="#fff"
                            stroke-width="1.7"
                          />
                        </svg>
                      </span>
                      <input :type="showConfirmPwd ? 'text' : 'password'" v-model="confirm_password" class="form-control pe-5" placeholder="Confirm Password" required />
                      <button type="button" class="btn position-absolute end-0 top-0 h-100 px-3 border-0 bg-transparent" @click="showConfirmPwd = !showConfirmPwd" aria-label="Toggle password">
                        <svg
                          v-if="!showConfirmPwd"
                          width="20"
                          height="20"
                          viewBox="0 0 24 24"
                          fill="none"
                        >
                          <path
                            d="M2.5 12s3.7-6.5 9.5-6.5S21.5 12 21.5 12 17.8 18.5 12 18.5 2.5 12 2.5 12z"
                            stroke="#fff"
                            stroke-width="1.7"
                          />
                          <circle
                            cx="12"
                            cy="12"
                            r="3"
                            stroke="#fff"
                            stroke-width="1.7"
                          />
                        </svg>
                        <svg
                          v-else
                          width="20"
                          height="20"
                          viewBox="0 0 24 24"
                          fill="none"
                        >
                          <path d="M3 3l18 18" stroke="#fff" stroke-width="1.7" />
                          <path
                            d="M6 6.8C3.8 8.4 2.5 12 2.5 12s3.7 6.5 9.5 6.5c1.6 0 3-.3 4.2-.8M16.5 8.2C15.2 7.6 13.7 7.5 12 7.5 6.2 7.5 2.5 12 2.5 12"
                            stroke="#fff"
                            stroke-width="1.7"
                          />
                        </svg>
                      </button>
                    </div>
                  </div>
                </div>

                <!-- Step 2: Personal Details -->
                <div v-if="step === 2">
                  <div class="mb-3">
                    <label class="form-label">Address</label>
                    <div class="input-shell">
                      <span class="left-ico">
                        <!-- MapPinHouse Icon -->
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                          <path d="M13 15V17M11 15V17M9.5 11H14.5M12 19.5c-1.435 0-2.153 0-2.59-.047-.55-.06-1.02-.185-1.414-.579-.394-.394-.519-.863-.58-1.413-.046-.437-.046-1.155-.046-2.59V9.04c0-1.36 0-2.04.175-2.646.153-.53.383-.995.67-1.373.287-.378.626-.66 1.005-.847.434-.214 1.043-.214 2.59-.214s2.156 0 2.59.214c.379.187.718.47 1.005.847.287.378.517.843.67 1.373.175.606.175 1.286.175 2.646v5.83c0 1.435 0 2.153-.047 2.59-.06.55-.185 1.02-.579 1.414-.394.394-.863.518-1.413.579-.437.046-1.155.046-2.59.046z" stroke="#fff" stroke-width="1.7" />
                        </svg>
                      </span>
                      <input v-model="address" type="text" class="form-control" placeholder="Enter address" required />
                    </div>
                  </div>

                  <div class="mb-3">
                    <label class="form-label">Pincode</label>
                    <div class="input-shell">
                      <span class="left-ico">
                        <!-- LocateFixed Icon -->
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                          <path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2z" stroke="#fff" stroke-width="1.7" />
                          <path d="M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8z" stroke="#fff" stroke-width="1.7" />
                        </svg>
                      </span>
                      <input v-model="pincode" type="number" class="form-control" placeholder="Enter pincode" required />
                    </div>
                  </div>
                </div>

                <!-- Error -->
                <div v-if="error" class="alert-error mt-3">
                  {{ error }}
                </div>

                <!-- Buttons -->
                <div class="mt-4 mb-2">
                  <button v-if="step === 1" class="btn btn-cta w-100" type="button" @click="nextStep">Next</button>
                  <button v-if="step === 2" class="btn btn-cta w-100 mb-2" type="submit">Sign Up</button>
                  <button v-if="step === 2" class="btn btn-pill w-100" type="button" @click="prevStep">Back</button>
                </div>
              </form>

              <div class="small muted text-center mt-3">
                Already have an account? <a href="/login" class="linkish">Log in here</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Floating decorative elements -->
    <div class="floating-dots" style="top: 20%; left: 10%;"></div>
    <div class="floating-dots" style="top: 60%; right: 15%; animation-delay: 2s;"></div>
    <div class="floating-dots" style="top: 40%; left: 80%; animation-delay: 4s;"></div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { callApi } from '@/utils.js'
import { useRouter } from "vue-router"

const router = useRouter();

const nav = ref(["About", "Contact", "Privacy", "Terms"]);
const step = ref(1)

const username = ref("")
const email = ref("")
const password = ref("")
const confirm_password = ref("")
const address = ref("")
const pincode = ref("")
const error = ref("")
const showPwd = ref(false)
const showConfirmPwd = ref(false)

const nextStep = () => {
  if (password.value !== confirm_password.value) {
    error.value = "Passwords do not match.";
    return;
  }
  if (!username.value || !email.value || !password.value) {
      error.value = "Please fill in all required fields.";
      return;
  }
  error.value = "";
  step.value = 2;
}

const prevStep = () => {
  step.value = 1;
}

const signup = async () => {
    if (!address.value || !pincode.value) {
        error.value = "Please fill in all required fields.";
        return;
    }
    error.value = "";

    const data = {
        "username": username.value,
        "email": email.value,
        "password": password.value,
        "confirm_password": confirm_password.value,
        "address": address.value,
        "pincode": pincode.value
    }

    const { ok, status, resData } = await callApi("signup", "POST", data)

    if (ok) {
        router.push('/login')
    } else {
        error.value = resData.message
    }
}
</script>

<style>
:root {
  --aerospace: #FE4B01;
  --silver: #B2B2B2;
  --calamansi: #E4FEA3;
  --orange: #FE733A;
  --tan: #D6936D;
  --white: #FFFFFF;

  /* UI helpers */
  --bg: #0d0706;
  --card: #151010;
  --muted: rgba(255, 255, 255, .65);
  --border: rgba(255, 255, 255, .08);
  --glass: rgba(255, 255, 255, .06);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", sans-serif;
  background: radial-gradient(1200px 500px at 50% 20%, rgba(254, 115, 58, .22), rgba(254, 75, 1, .08) 30%, transparent 65%),
    radial-gradient(900px 600px at 60% 85%, rgba(254, 75, 1, .12), transparent 60%),
    #0a0808;
  color: var(--white);
  overflow-x: hidden;
}

/* rounded screen look */
.screen {
  background: radial-gradient(100% 40% at 50% -5%, rgba(255, 255, 255, .06), transparent),
    rgba(10, 8, 8, .85);
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, .06),
    0 40px 120px rgba(0, 0, 0, .65);
  padding: 26px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* NAVBAR */
.nav-glass {
  background: linear-gradient(180deg, rgba(255, 255, 255, .06), rgba(255, 255, 255, .03));
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 10px 14px;
  backdrop-filter: blur(6px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, .35), inset 0 1px rgba(255, 255, 255, .18);
}

.brand-logo {
  width: 28px;
  height: 28px;
  border-radius: 12px;
  background: radial-gradient(circle at 30% 30%, #fff8, #fff0 40%), linear-gradient(135deg, var(--orange), var(--aerospace));
  filter: drop-shadow(0 0 10px rgba(254, 75, 1, .35));
  margin-right: 10px;
}

.nav-link {
  color: var(--silver);
  opacity: .95;
  font-weight: 500
}

.nav-link:hover {
  color: #fff
}

.btn-pill {
  border-radius: 999px;
  padding: .55rem 1rem;
  font-weight: 600;
  border: 1px solid var(--border);
  color: #fff;
  background: var(--glass);
  backdrop-filter: blur(6px);
}

.btn-cta {
  border-radius: 999px;
  padding: .6rem 1rem;
  font-weight: 700;
  background: radial-gradient(100% 120% at 30% 20%, #fff2, transparent 45%),
    linear-gradient(90deg, var(--orange), var(--aerospace));
  border: 0;
  box-shadow: 0 10px 24px rgba(254, 75, 1, .45), inset 0 1px rgba(255, 255, 255, .35);
}

.btn-cta:hover {
  filter: brightness(1.05)
}

.btn-pill:hover {
  background-color: rgba(255, 255, 255, .1)
}

/* Signup Section */
.login-section {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px 20px;
  position: relative;
}

.login-container {
  max-width: 1040px;
  width: 100%;
  overflow: hidden;
}

.art-wrap {
  height: 560px;
  position: relative;
  overflow: visible;
  border-right: 1px solid var(--border);
}

.art-img {
  position: absolute;
      bottom: -32px; /* sit a bit below the panel */
      left: -24px;
      width: 125%; /* scale up so the hand reaches across */
      max-width: none;
      z-index: 1; /* sits under the form column which has z-index:2 */
      user-select: none;
      pointer-events: none;
}

.art-img.floaty {
  animation: floaty 5s ease-in-out infinite;
}

@keyframes floaty {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-12px); }
}

.form-column {
  padding: 40px;
  position: relative;
  z-index: 2;
}

.form-wrap {
  max-width: 400px;
  margin: 0 auto;
}

.login-title {
  font-size: 2.2rem;
  font-weight: 700;
  margin-bottom: 30px;
  text-align: center;
}

.form-label {
  font-weight: 600;
  color: var(--white);
  margin-bottom: 8px;
  display: block;
  font-size: 0.95rem;
}

.input-shell {
  position: relative;
}

.input-shell .left-ico {
  position: absolute;
  top: 50%;
  left: 16px;
  transform: translateY(-50%);
  color: var(--muted);
  pointer-events: none;
  opacity: 0.8;
}

.form-control {
  height: 48px;
  background: rgba(255, 255, 255, .06);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding-left: 48px;
  color: var(--white);
  font-size: 0.95rem;
  transition: all 0.3s;
}

.form-control:focus {
  border-color: var(--aerospace);
  box-shadow: 0 0 0 3px rgba(254, 75, 1, .2);
  background: rgba(255, 255, 255, .08);
  color: white;
}

.form-control::placeholder {
  color: var(--white);
}

.btn-cta.w-100,
.btn-pill.w-100 {
  height: 48px;
  font-size: 1rem;
}

.alert-error {
  background: rgba(254, 75, 1, 0.2);
  border: 1px solid var(--aerospace);
  color: var(--white);
  padding: 10px 16px;
  border-radius: 12px;
  font-size: 0.9rem;
  text-align: center;
}

.muted {
  color: var(--muted);
  font-size: 0.9rem;
}

.linkish {
  color: var(--aerospace);
  text-decoration: none;
  font-weight: 600;
}

.linkish:hover {
  text-decoration: underline;
  color: var(--orange);
}

/* Glossy Card Style */
.glossy-card {
  position: relative;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, .08) 0%, rgba(255, 255, 255, .03) 28%, rgba(0, 0, 0, .50) 100%),
    radial-gradient(140% 120% at 50% -10%, rgba(254, 115, 58, .55), rgba(254, 75, 1, .15) 35%, transparent 60%),
    #130e0e;
  border: 1px solid var(--border);
  border-radius: 22px;
  box-shadow:
    inset 0 1px rgba(255, 255, 255, .25),
    inset 0 20px 60px rgba(255, 255, 255, .04),
    0 18px 40px rgba(0, 0, 0, .6),
    0 20px 60px rgba(254, 75, 1, .15);
  overflow: hidden;
  transition: transform 0.3s, box-shadow 0.3s;
}

.glossy-card::before {
  content: "";
  position: absolute;
  left: -8%;
  right: -8%;
  top: -10%;
  height: 55%;
  background: linear-gradient(to bottom, rgba(255, 255, 255, .35), rgba(255, 255, 255, 0));
  filter: blur(18px);
  pointer-events: none;
}

.glossy-card::after {
  content: "";
  position: absolute;
  inset: auto -30% -30% -30%;
  height: 55%;
  background: radial-gradient(60% 120% at 50% 0%, rgba(254, 75, 1, .25), transparent 65%);
  filter: blur(22px);
  pointer-events: none;
}

.glossy-card:hover {
  transform: translateY(-5px);
  box-shadow:
    inset 0 1px rgba(255, 255, 255, .25),
    inset 0 20px 60px rgba(255, 255, 255, .04),
    0 22px 48px rgba(0, 0, 0, .7),
    0 24px 72px rgba(254, 75, 1, .2);
}

/* Decorative Elements */
.floating-dots {
  position: absolute;
  width: 4px;
  height: 4px;
  background: var(--aerospace);
  border-radius: 50%;
  animation: float 10s infinite;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0) translateX(0);
  }
  25% {
    transform: translateY(-20px) translateX(10px);
  }
  50% {
    transform: translateY(10px) translateX(-10px);
  }
  75% {
    transform: translateY(-10px) translateX(5px);
  }
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .art-img {
    width: 140%;
    bottom: -30%;
  }
}

@media (max-width: 768px) {
  .art-column {
    height: 300px;
    border-right: none;
    border-bottom: 1px solid var(--border);
  }
  .form-column {
    padding: 30px 20px;
  }
  .login-title {
    font-size: 1.8rem;
  }
}
</style>