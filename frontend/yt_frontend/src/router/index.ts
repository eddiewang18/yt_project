import Home from '@/components/Home.vue'
import Register from '@/components/Register.vue'
import { createRouter, createWebHistory } from 'vue-router'
import login from '@/components/login.vue'
import FinishRegister from '@/components/finishRegister.vue'
import EmailSend from '@/components/emailSend.vue'

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
        ]
    }
)

export default router