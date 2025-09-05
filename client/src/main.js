import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { tokenChecker } from './utils'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'


const app = createApp(App)
app.use(router)
app.use(createPinia())
tokenChecker()
app.mount('#app')

