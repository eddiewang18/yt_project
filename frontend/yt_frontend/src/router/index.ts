import Home from '@/components/Home.vue'
import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter(
    {
        history: createWebHistory(),
        routes: [
            {
                path: '/',
                component:Home
            }
        ]
    }
)

export default router