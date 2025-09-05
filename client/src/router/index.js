import { createRouter, createWebHistory } from 'vue-router';
import { dataStore } from '../store/data';

// import Home from '../views/Home.vue'
// import Login from '../views/Login.vue';
// import Signup from '../views/Signup.vue';

// Lazy Load
const Home = () => import('@/views/Home.vue');
const Login = () => import('@/views/Login.vue');
const Signup = () => import('@/views/Signup.vue');
const Dashboard = () => import('@/views/Dashboard.vue')
const Lot = () => import('@/views/Lot.vue')
const AdminUsers = () => import('@/views/AdminUsers.vue')
const AvailableLots = () => import('@/views/AvailableLots.vue')
const ParkingHistory = () => import('@/views/ParkingHistory.vue')
const UserSummary = () => import('@/views/Summary/User.vue')
const AdminSummary = () => import('@/views/Summary/Admin.vue')
const Notification = () => import('@/views/Notification.vue')
const Payment = () => import('@/views/Payment.vue')

const routes = [
    {
        path: '/',
        component: Home,
        meta: {
            requireAuth: false
        }
    },
    {
        path: '/login', 
        component: Login,
        meta: {
            requireAuth: false
        }
    },
    {
        path: '/signup', 
        component: Signup,
        meta: {
            requireAuth: false
        }
    },
    {
        path: '/dashboard', 
        component: Dashboard,
        meta: {
            requireAuth: true
        },
        children: [
            {
                path: 'admin-summary',
                component: AdminSummary,
                meta: {
                    requireAuth: true,
                    role: 'admin'
                }
            },
            {
                path: 'user-summary',
                component: UserSummary,
                meta: {
                    requireAuth: true,
                    role: 'user'
                }
            },
            {
                path: 'lot',
                component: Lot,
                meta: {
                    requireAuth: true,
                    role: 'admin'
                }
            },
            {
                path: 'users',
                component: AdminUsers,
                meta: {
                    requireAuth: true,
                    role: 'admin'
                }
            },
            {
                path: 'available_lots',
                component: AvailableLots,
                meta: {
                    requireAuth: true,
                    role: 'user'
                }
            },
            {
                path: 'parking-history',
                component: ParkingHistory,
                meta: {
                    requireAuth: true,
                    role: 'user'
                }
            },
            
            {
                path: 'notification',
                component: Notification,
                meta: {
                    requireAuth: true,
                    role: 'user'
                }
            },
            {
                path: 'payment',
                component: Payment,
                meta: {
                    requireAuth: true,
                    role: 'admin'
                }
            }

        ]
    }
    
]

const router = createRouter(
    {history: createWebHistory(),
    routes
    }
)

router.beforeEach((to,from,next) => {
    const data_store = dataStore()
    const role = data_store.role

    if (to.meta.requireAuth) {
        if (role) {
            if (to.meta.role && to.meta.role !== role) {
                next('/unauthorized')
            } else {
                next()
            }
        } else {
            next('/login')
        }
    }
     else {
        next()
    }

    
})


export default router;