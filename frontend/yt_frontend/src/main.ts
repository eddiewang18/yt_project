import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import "bootstrap-icons/font/bootstrap-icons.css"

// 引入FontAwesome核心
import { library } from '@fortawesome/fontawesome-svg-core'
// 引入FontAwesome组件
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
// 引入你需要的图标
import { faCircleCheck } from '@fortawesome/free-solid-svg-icons'
import { faCircleXmark } from '@fortawesome/free-solid-svg-icons'
import { faCopy } from '@fortawesome/free-solid-svg-icons';
import { faPaperclip } from '@fortawesome/free-solid-svg-icons';
import { faArrowUp } from '@fortawesome/free-solid-svg-icons';
import { faEye } from '@fortawesome/free-solid-svg-icons';
import { faEyeSlash } from '@fortawesome/free-solid-svg-icons';
import { faPaperPlane } from '@fortawesome/free-solid-svg-icons';
import { faHouse } from '@fortawesome/free-solid-svg-icons';

library.add(faCircleCheck)
library.add(faCircleXmark)
library.add(faCopy)
library.add(faPaperclip)
library.add(faArrowUp)
library.add(faEye)
library.add(faEyeSlash)
library.add(faPaperPlane)
library.add(faHouse)
const app = createApp(App);

// 注册FontAwesome组件
app.component('font-awesome-icon', FontAwesomeIcon)

app.use(router);
app.mount("#app");
