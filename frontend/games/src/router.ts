import {createWebHistory, createRouter} from 'vue-router';
import Home from './views/Home.vue';
import Games from './views/Games.vue';
import AddGame from './views/AddGame.vue';


const routes = [
    {path: '/', name: "Home", component: Home},
    {path: '/games', name: "Games", component: Games},
    {path: '/add_game', name: "Add Game", component: AddGame},
];

const router = createRouter({
    routes,
    history: createWebHistory(),
})

export default router;
