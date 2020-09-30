import {createWebHistory, createRouter} from 'vue-router';
import Games from './views/Games.vue';


const routes = [
    {path: '/games', name: "Games", component: Games},
];

const router = createRouter({
    routes,
    history: createWebHistory(),
})

export default router;
