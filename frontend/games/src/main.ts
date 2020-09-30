import {createApp} from 'vue';
import App from './views/Home.vue';
import "./css/main.scss";

import router from './router';

const app = createApp(App);
app.use(router);
app.mount('#app');
//createApp(App).mount('#app');
