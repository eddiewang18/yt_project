import Home from '@/components/Home.vue'
import Register from '@/components/Register.vue'
import { createRouter, createWebHistory } from 'vue-router'
import login from '@/components/login.vue'
import FinishRegister from '@/components/finishRegister.vue'
import EmailSend from '@/components/emailSend.vue'
import Admin_login from '@/components/admin_login.vue'
import Admin_home from '@/components/admin_home.vue'
import AdminDataAnalasis from '@/components/AdminDataAnalasis.vue'
import Yt_analysis from '@/components/Yt_analysis.vue'
import AdminUserAnalysis from '@/components/AdminUserAnalysis.vue'

// const router = createRouter(
//     {
//         history: createWebHistory(),
//         routes: [
//             {
//                 path: '/',
//                 component:Home
//             },
//             {
//                 path: '/register',
//                 component: Register
                
//             },
//             {
//                 path: '/login',
//                 component: login
                
//             },
//             {
//                 path: '/finish',
//                 component: FinishRegister
                
//             },
//             {
//                 path: '/sendMail/:email',
//                 component: EmailSend
                
//             },
//             {
//                 path: '/admin_login',
//                 component: Admin_login
                
//             },
//         ]
//     }
// )
const router = createRouter(
    {
        history: createWebHistory(),
        routes: [
            {
                path: '/',
                component:Home
            },
            {
                path: '/register',
                component: Register
                
            },
            {
                path: '/login',
                component: login
                
            },
            {
                path: '/finish',
                component: FinishRegister
                
            },
            {
                path: '/sendMail/:email',
                component: EmailSend
                
            },
            {
                path: '/admin_login',
                component: Admin_login
                
            },
            {
                path: "/admin/home",
                component: Admin_home,
                children: [
                    {
                        path: "data_analasis",
                        component:AdminDataAnalasis
                    },
                    {
                        path: "analysis01",
                        component:Yt_analysis
                    },
                    {
                        path: "analysis02",
                        component:AdminUserAnalysis
                    }
                ]
            }
        ]
    }
)
export default router

