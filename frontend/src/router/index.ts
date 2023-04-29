import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      meta: {'title': 'Fire RSS'},
      component: () => import('@/layout/LayoutMain.vue'),
    },
    {
      path: '/auth',
      name: 'auth',
      component: () => import('@/layout/LayoutMain.vue'),
      children: [
        {
          path: 'signin',
          name: 'signin',
          component: () => import('@/views/auth/SignIn.vue'),
          meta: { title: 'Sign In' },
        },
        {
          path: 'signup',
          name: 'signup',
          component: () => import('@/views/auth/SignUp.vue'),
          meta: { title: 'Sign Up' },
        },
      ],
    },

  ]
})

export default router
