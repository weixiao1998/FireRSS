import { createRouter, createWebHistory } from 'vue-router'

import MainLayout from '@/layout/MainLayout.vue'
import EmptyLayout from '@/layout/EmptyLayout.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      meta: {'title': 'Fire RSS'},
      component: MainLayout,
    },
    {
      path: '/auth',
      name: 'auth',
      component: EmptyLayout,
      children: [
        {
          path: 'sign-in',
          name: 'sign-in',
          alias: ['login'],
          component: () => import('@/views/auth/SignIn.vue'),
          meta: { title: 'Sign In' },
        },
        {
          path: 'sign-up',
          name: 'sign-up',
          component: () => import('@/views/auth/SignUp.vue'),
          meta: { title: 'Sign Up' },
        },
      ],
    },

  ]
})

export default router
