import {createWebHistory, createRouter} from 'vue-router';
import Home from './views/Home.vue';
import Games from './views/Games.vue';


const routes = [
    {path: '/', name: "Home", component: Home},
    {path: '/games', name: "Games", component: Games},
];

const router = createRouter({
    routes,
    history: createWebHistory(),
})

export default router;
