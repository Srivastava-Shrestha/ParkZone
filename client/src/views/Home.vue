<template>
  <div class="screen">
    <!-- NAV -->
    <div class="nav-glass mb-4">
      <div class="d-flex align-items-center">
        <div class="d-flex align-items-center me-3">
          <div>
            <img class="brand-logo" src="/src/assets/logo.png"></img>
          </div>
          <strong>ParkZone</strong>
        </div>
        <ul class="nav me-auto">
          <li class="nav-item" v-for="(n, i) in nav" :key="i">
            <a href="#" class="nav-link px-3">{{ n }}</a>
          </li>
        </ul>
        <div class="d-flex gap-2">
          <a href="/login" class="btn btn-pill">Login</a>
          <a href="/signup" class="btn btn-cta">Sign up for free</a>
        </div>
      </div>
    </div>
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="operations-badge">
        <div class="badge-dot"></div>
        <span>Unified Parking System</span>
      </div>
      <h1>Smart Solutions for Modern Parking Management<br /></h1>
      <p class="hero-description">
        Seamlessly manage, book, and monitor parking spaces with ParkZone A unified platform offering real-time availability, reservations, payments, and insights to simplify urban parking.
      </p>
      <div class="hero-buttons">
        <a href="/signup" class="btn btn-primary-custom">Book Now</a>
        <!-- <button class="btn btn-secondary-custom">Book a demo</button> -->
      </div>
      <!-- Glossy Cards -->
      <div class="cards-container">
        <!-- Cloud Inventory Card -->
        <div class="glossy-card">
          <div class="card-title">Overall Stats</div>
          <div class="card-sub">Overview of reservations, bookings, spend and Top visiting Lot</div>

          <div class="inv-item">
            <div class="d-flex align-items-center">
              <span class="dot"></span>
              <span class="fw-semibold">Total Reservations</span>
            </div>
            <div class="d-flex align-items-center gap-2">
              <span class="badge-soft">100</span>
              <div class="gradient-bar"></div>
            </div>
          </div>

          <div class="inv-item">
            <div class="d-flex align-items-center">
              <span class="dot"></span>
              <span class="fw-semibold">Total Bookings</span>
            </div>
            <div class="d-flex align-items-center gap-2">
              <span class="badge-soft">85</span>
              <div class="gradient-bar"></div>
            </div>
          </div>

          <div class="inv-item">
            <div class="d-flex align-items-center">
              <span class="dot"></span>
              <span class="fw-semibold">Total Amount spent</span>
            </div>
            <div class="d-flex align-items-center gap-2">
              <span class="badge-soft">₹25,000</span>
              <div class="gradient-bar"></div>
            </div>
          </div>

          <div class="inv-item">
            <div class="d-flex align-items-center">
              <span class="dot"></span>
              <span class="fw-semibold">Most Visited Lot</span>
            </div>
            <div class="d-flex align-items-center gap-2">
              <span class="badge-soft">City Center</span>
              <div class="gradient-bar"></div>
            </div>
          </div>
        </div>

        <!-- Accounts With Critical Risk Score Card -->
        <div class="glossy-card">
          <div class="d-flex align-items-center justify-content-between">
            <div>
              <div class="card-title">Monthly Reservation Distribution</div>
              <div class="small d-flex align-items-center gap-3 small-hint">
                <span class="d-flex align-items-center gap-1">
                  <span class="dot" style="width:8px;height:8px"></span> Reservation per month
                </span>
            
        
              </div>
            </div>
          </div>

          <div class="bars">
            <div v-for="(h, i) in bars" :key="'b' + i" class="bar" :class="[{ 'bar--muted': i !== 5 }]"
              style="height:100%">
              <span :style="{ height: h + '%' }"></span>
              <!-- <span v-if="i===5" class="bar-label">690</span> -->
            </div>
          </div>

          <div class="d-flex justify-content-between small-hint mt-2" style="font-size:.8rem">
            <span>Jan</span>
            <span>Feb</span>
            <span>Mar</span>
            <span>Apr</span>
            <span>May</span>
            <span>Jun</span>
            <span>Jul</span>
            <span>Aug</span>
            <span>Sep</span>
          </div>
        </div>

        <!-- Assets With Location Card -->
        <div class="glossy-card position-relative overflow-hidden">
          <div class="d-flex align-items-center justify-content-between">
            <div>
              <div class="card-title">Booking Status</div>
              <div class="display-6 fw-bold" style="line-height:1">68</div>
              <div class="small-hint">Reservation by Lot</div>
            </div>
          </div>
          <div class="planet"></div>
          <div class="orbit"></div>
        </div>
      </div>
    </section>
    <!-- Partners Section -->
    <section class="partners-section">
      <p class="partners-title">Revolutionizing how cities park, One Spot at a Time!</p>
    </section>
    <!-- Floating decorative elements -->
    <div class="floating-dots" style="top: 20%; left: 10%;"></div>
    <div class="floating-dots" style="top: 60%; right: 15%; animation-delay: 2s;"></div>
    <div class="floating-dots" style="top: 40%; left: 80%; animation-delay: 4s;"></div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
// Navbar
const nav = ref(["About", "Contact", "Privacy", "Terms"]);
const bars = ref([26, 32, 45, 40, 52, 86, 48, 35, 30]);
let observer;
onMounted(() => {
  console.log('CyberRisk Platform Loaded');
  observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.animation = 'float 10s infinite';
      }
    });
  });
  document.querySelectorAll('.glossy-card').forEach((card) => {
    observer.observe(card);
  });
});
onBeforeUnmount(() => {
  if (observer) observer.disconnect();
});
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

/* Hero Section */
.hero-section {
  padding: 20px 20px;
  text-align: center;
  position: relative;
}

.operations-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(254, 75, 1, 0.2);
  border: 1px solid var(--aerospace);
  padding: 6px 16px;
  border-radius: 20px;
  margin-bottom: 30px;
  font-size: 0.9rem;
}

.badge-dot {
  width: 8px;
  height: 8px;
  background: var(--aerospace);
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {

  0%,
  100% {
    opacity: 1;
  }

  50% {
    opacity: 0.5;
  }
}

h1 {
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: 30px;
  line-height: 1.2;
}

.hero-description {
  color: rgba(255, 255, 255, 0.7);
  max-width: 600px;
  margin: 0 auto 40px;
  font-size: 1.1rem;
  line-height: 1.6;
}

.hero-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
  margin-bottom: 80px;
}

.btn-primary-custom {
  background: var(--aerospace);
  color: var(--white);
  border: none;
  padding: 12px 32px;
  border-radius: 25px;
  font-weight: 600;
  transition: all 0.3s;
}

.btn-primary-custom:hover {
  background: var(--orange);
  transform: translateY(-2px);
}

.btn-secondary-custom {
  background: transparent;
  color: var(--white);
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 12px 32px;
  border-radius: 25px;
  font-weight: 600;
  transition: all 0.3s;
}

.btn-secondary-custom:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: var(--white);
}

/* Glossy Cards Section */
.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Glossy Card - From gpt.vue */
.glossy-card {
  position: relative;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, .08) 0%, rgba(255, 255, 255, .03) 28%, rgba(0, 0, 0, .50) 100%),
    radial-gradient(140% 120% at 50% -10%, rgba(254, 115, 58, .55), rgba(254, 75, 1, .15) 35%, transparent 60%),
    #130e0e;
  border: 1px solid var(--border);
  border-radius: 22px;
  padding: 20px;
  box-shadow:
    inset 0 1px rgba(255, 255, 255, .25),
    inset 0 20px 60px rgba(255, 255, 255, .04),
    0 18px 40px rgba(0, 0, 0, .6),
    0 20px 60px rgba(254, 75, 1, .15);
  overflow: hidden;
  transition: transform 0.3s, box-shadow 0.3s;
}

.glossy-card::before {
  /* Top sheen */
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
  /* Bottom orange glow */
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

.card-title {
  font-weight: 700;
  font-size: 1.05rem;
  margin-bottom: .25rem;
  position: relative;
  z-index: 1;
}

.card-sub {
  color: var(--silver);
  font-size: .9rem;
  margin-bottom: 1rem;
  position: relative;
  z-index: 1;
}

/* List inside left card */
.inv-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: .55rem .7rem;
  border-radius: 12px;
  margin: .35rem 0;
  background: rgba(255, 255, 255, .03);
  border: 1px solid rgba(255, 255, 255, .06);
  position: relative;
  z-index: 1;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, #fff8, #fff0 40%), linear-gradient(135deg, var(--orange), var(--aerospace));
  box-shadow: 0 0 12px rgba(254, 75, 1, .6);
  margin-right: .55rem;
}

.badge-soft {
  border-radius: 10px;
  padding: .2rem .45rem;
  font-size: .8rem;
  background: rgba(255, 255, 255, .06);
  border: 1px solid rgba(255, 255, 255, .08);
  color: #fff;
}

.gradient-bar {
  width: 34px;
  height: 10px;
  border-radius: 6px;
  background: linear-gradient(90deg, rgba(254, 115, 58, .95), rgba(254, 75, 1, .9));
  box-shadow: 0 0 10px rgba(254, 75, 1, .45);
}

/* Center card bars */
.bars {
  display: flex;
  align-items: flex-end;
  gap: 10px;
  height: 180px;
  margin-top: .7rem;
}

.bar {
  flex: 1;
  background: linear-gradient(180deg, rgba(255, 255, 255, .14), rgba(255, 255, 255, .04) 25%, rgba(0, 0, 0, .5) 100%);
  border: 1px solid rgba(255, 255, 255, .08);
  border-radius: 10px 10px 6px 6px;
  position: relative;
  overflow: hidden;
}

.bar:hover {
  background: linear-gradient(to top, var(--aerospace), rgba(254, 75, 1, 0.3));
}

.bar.highlight {
  background: linear-gradient(to top, var(--aerospace), var(--orange));
}

.bar>span {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(180deg, rgba(254, 115, 58, .85), rgba(254, 75, 1, .85));
  box-shadow: 0 10px 18px rgba(254, 75, 1, .32), inset 0 1px rgba(255, 255, 255, .35);
  border-radius: 9px 9px 6px 6px;
  display: block;
}

.bar--muted>span {
  background: linear-gradient(180deg, rgba(255, 255, 255, .14), rgba(255, 255, 255, .08));
  box-shadow: none;
}

.bar-label {
  position: absolute;
  top: -28px;
  left: 50%;
  transform: translateX(-50%);
  font-size: .8rem;
  background: rgba(255, 255, 255, .08);
  padding: .15rem .4rem;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, .12);
  white-space: nowrap;
}

/* Right card planet */
.planet {
  position: absolute;
  right: -6%;
  bottom: -18%;
  width: 75%;
  aspect-ratio: 1/1;
  border-radius: 50%;
  background:
    radial-gradient(45% 45% at 30% 30%, rgba(255, 255, 255, .08), rgba(255, 255, 255, 0) 55%),
    radial-gradient(60% 60% at 65% 65%, rgba(0, 0, 0, .65), rgba(0, 0, 0, .95)),
    radial-gradient(70% 70% at 55% 45%, rgba(214, 147, 109, .45), rgba(214, 147, 109, .05) 70%),
    #2b1e1c;
  box-shadow:
    inset -10px -10px 40px rgba(0, 0, 0, .65),
    0 0 0 6px rgba(254, 75, 1, .35),
    0 0 38px rgba(254, 75, 1, .45);
  overflow: hidden;
}

.planet::after {
  /* bright limb */
  content: "";
  position: absolute;
  inset: -10%;
  border-radius: 50%;
  background: conic-gradient(from 200deg, rgba(254, 75, 1, .7), rgba(254, 115, 58, .45), transparent 40%, transparent);
  mix-blend-mode: screen;
  filter: blur(1px);
}

.orbit {
  position: absolute;
  width: 120%;
  height: 120%;
  border-radius: 50%;
  border: 1px solid rgba(254, 75, 1, .3);
  right: -15%;
  bottom: -25%;
  transform: rotate(-18deg);
}

.small-hint {
  font-size: .9rem;
  color: var(--silver);
  position: relative;
  z-index: 1;
}

/* Partners Section */
.partners-section {
  margin-top: 100px;
  padding: 40px 20px;
  text-align: center;
}

.partners-title {
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 30px;
  font-size: 1rem;
}

.partners-grid {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 40px;
  max-width: 1000px;
  margin: 0 auto;
}

.partner-logo {
  color: rgba(255, 255, 255, 0.4);
  font-size: 1.2rem;
  font-weight: 600;
  transition: color 0.3s;
}

.partner-logo:hover {
  color: rgba(255, 255, 255, 0.7);
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

  0%,
  100% {
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

.navbar-toggler {
  border-color: rgba(255, 255, 255, 0.25);
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
  /* border-radius:28px; */
  background: radial-gradient(100% 40% at 50% -5%, rgba(255, 255, 255, .06), transparent),
    rgba(10, 8, 8, .85);
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, .06),
    0 40px 120px rgba(0, 0, 0, .65);
  padding: 26px;
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
  background: radial-gradient(circle at 30% 30%, #fff, #fff 6px, transparent 7px) no-repeat,
    radial-gradient(70% 100% at 30% 30%, var(--orange), var(--aerospace));
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
</style>