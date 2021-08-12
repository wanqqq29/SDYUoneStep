import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      // { 
      //   path: '/',
      //   component: () => import('pages/os_index.vue'),
      // },
      { 
        path:'tool',
        component:()=> import('pages/os_tool.vue'), 
      },
      { 
        path:'/',
        component:()=> import('pages/os_tool.vue'), 
      },
      {
        path:'list',
        name:'list',
        component:()=> import('pages/pagess/list.vue'),
      },
      { 
        path: 'test',
        component: () => import('pages/test.vue')
      },
      { 
        path: 'guidmap',
        component: () => import('pages/pagess/guidmap.vue')
      },
    ],
  },


  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue'),
  },
  
];

export default routes;
