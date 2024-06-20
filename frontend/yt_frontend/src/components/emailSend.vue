<template>
    <div class="container">
        <div class="head">
            <div class="title animate">
                驗證信已寄至{{ $route.params.email }}，請至註冊之信箱收信
                <span class="animate icon">
                    <font-awesome-icon :icon="['fas', 'paper-plane']" class="fa-2x" style="color: #6fa4ce;" />
                </span>
            </div>
        </div>
        <div class="body">
            <span class="qmsg">
                未收到驗證信?
            </span>
            <button @click="reSendMail" class="field_btn">重新寄信</button>
        </div>
    </div>
    <div id="loadingMsg" class="hide">系統已重新寄出驗證信，請稍後...</div>

</template>

<script>
export default {
    name:"EmailSend"
}
</script>

<script setup>
import { useRoute } from 'vue-router';
import axios from 'axios'
const route = useRoute();
let resend_email = route.params.email;

async function reSendMail() {
    try {
        let loadingMsg = document.getElementById("loadingMsg");
        loadingMsg.classList.remove("hide");
        loadingMsg.classList.add("show");
        let api_url = "http://127.0.0.1:8000/account/register/";
        let response = await axios.put(api_url, { "email": resend_email })
        let email = response.data.email
        let is_active = response.data.is_active;
        if (is_active == 'false') {
            loadingMsg.classList.remove("show");
            loadingMsg.classList.add("hide");
            window.location.href = `http://localhost:5173/sendMail/${email}`;            
        } else if (is_active == 'true') {
            window.location.href = `http://localhost:5173/finish/`;  
        }

    } catch (error) {
        console.log(error)
    }
}

</script>

<style scoped>
/* 全局样式 */
body {
    font-family: 'Arial', sans-serif;
    background: linear-gradient(to right, #ff758c, #ff7eb3);
    color: #333;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* 容器样式 */
.container {
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    padding: 20px;
    max-width: 500px;
    width: 100%;
}

/* 标题样式 */
.head .title {
    font-size: 24px;
    font-weight: bold;
    color: #ff758c;
    text-align: center;
    margin-bottom: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* 动画图标样式 */
.head .title .animate.icon {
    margin-left: 10px;
    animation: bounce 2s infinite;
}

/* Bounce 动画 */
@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-20px);
    }
    60% {
        transform: translateY(-10px);
    }
}

/* 消息样式 */
.body .qmsg {
    display: block;
    font-size: 18px;
    color: #ff758c;
    text-align: center;
    margin-bottom: 20px;
}

/* 按钮样式 */
.body .field_btn {
    display: block;
    background: #ff758c;
    color: #fff;
    border: none;
    padding: 15px 25px;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s ease;
    font-size: 16px;
    margin: 0 auto;
    text-align: center;
}

.body .field_btn:hover {
    background: #e94b67;
}

#loadingMsg {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    background-color: rgba(0, 0, 0, 0.8);
    color: #fff;
    padding: 10px 20px;
    border-radius: 5px;
    font-size: 16px;
    animation: bounce 1s infinite alternate; /* 增加上下跳動的動畫效果 */
}

.hide{
    display: none;
}

.show{
    display: block;
}

</style>