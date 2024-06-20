<template>
    <div class="head_icon"><RouterLink to="/"><font-awesome-icon :icon="['fas', 'house']" class="fa-2x" style="color: #6099fb;" /></RouterLink> </div>
    <span v-if="loginStatus" class="username">{{ username }}</span>
<div class="container">

    <div class="header">

        <div class="title">
            在線Youtube轉mp3、mp4
        </div>
        <div class="userblock">
            <button v-if="!loginStatus" class="account-btn">
                <RouterLink to="/login">登入</RouterLink>
            </button>
            <button v-else @click="logout" class="account-btn">
                登出
            </button>
        </div>
    </div>
    <div class="body">
        <form action="">
            <div>
                <input v-model="yt_link" type="text" placeholder="請輸入Youtube連結">
            </div>
            <div class="button-group">
                <button @click.prevent="convertAudio('mp3')" class="convertBtn">轉MP3</button>
                <button @click.prevent="convertAudio('mp4')" class="convertBtn">轉MP4</button>
            </div>
        </form>

        <div>
            <div class="sub_title">
                本日熱門-台灣
            </div>
            <div class="recommendation">
                <div v-for="(item , index) in ytData.TW" class="music_block" :id="item.video_id">
                    <img :src="item.img" alt="">
                    <a :id="'TW@a@'+index" :href="item.video_url" target="_blank"><font-awesome-icon :icon="['fas', 'paperclip']" style="color: #ffffff;" /></a>
                    <span class="music_title">{{item.title}}</span>
                    <button :id="'TW@btn@'+index" @click="copyLink"><font-awesome-icon :icon="['fas', 'copy']"  style="color: #ffffff;" /></button>
                </div>
            </div>
            <div class="sub_title">
                本日熱門-美國
            </div>
            <div class="recommendation">
                <div v-for="(item , index) in ytData.US" class="music_block" :id="item.video_id">
                    <img :src="item.img" alt="">
                    <a :href="item.video_url" target="_blank"><font-awesome-icon :icon="['fas', 'paperclip']" style="color: #ffffff;" /></a>
                    <span class="music_title">{{item.title}}</span>
                    <button><font-awesome-icon :icon="['fas', 'copy']"  style="color: #ffffff;" /></button>
                </div>
            </div>
            <div class="sub_title">
                本日熱門-日本
            </div>
            <div class="recommendation">
                <div v-for="(item , index) in ytData.JP" class="music_block" :id="item.video_id">
                    <img :src="item.img" alt="">
                    <a :href="item.video_url" target="_blank"><font-awesome-icon :icon="['fas', 'paperclip']" style="color: #ffffff;" /></a>
                    <span class="music_title">{{item.title}}</span>
                    <button><font-awesome-icon :icon="['fas', 'copy']"  style="color: #ffffff;" /></button>
                </div>
            </div>
            <div class="sub_title">
                本日熱門-南韓
            </div>
            <div class="recommendation">
                <div v-for="(item , index) in ytData.KR" class="music_block" :id="item.video_id">
                    <img :src="item.img" alt="">
                    <a :href="item.video_url" target="_blank"><font-awesome-icon :icon="['fas', 'paperclip']" style="color: #ffffff;" /></a>
                    <span class="music_title">{{item.title}}</span>
                    <button><font-awesome-icon :icon="['fas', 'copy']"  style="color: #ffffff;" /></button>
                </div>
            </div>

        </div>
    </div>
</div>
<button @click="scrollUp" class="fab"><font-awesome-icon :icon="['fas', 'arrow-up']" style="color: #ffffff;" /></button>

<div id="loadingMsg" class="hide">請稍後，正在轉檔中...</div>
<modal :msg="msg" :dynamicStatusClass :successFlag="successFlag" ref="msgModal"></modal>
</template>


<script >
export default {
    name:"Home"
}
</script>

<script setup>
import axios from 'axios'
import { ref , reactive } from 'vue'
import modal from './modal.vue'
import { useRouter } from 'vue-router'


let yt_link = ref(""); // 輸入的youtube連結
let msgModal = ref(null); // 指向 modal組件
let msg = ref(""); // modal 訊息
let dynamicStatusClass = ref("");
let successFlag = ref("");
const api_url = "http://127.0.0.1:8000/basic/home/";
let ytData = reactive({});
const router = useRouter();
getData()

let loginStatus = ref(localStorage.getItem("login"))
let access_token = localStorage.getItem("access_token")
let username = ref("");
if (access_token != null && getUsernameFromToken(access_token) != null) { 
    username.value = getUsernameFromToken(access_token)[0]
}
// Youtube轉檔
async function convertAudio(fileType) {
    if (yt_link.value.length === 0) { 
        msg.value = "youtube連結 不可空白"
        dynamicStatusClass.value = 'fail';
        successFlag.value = false;
        msgModal.value.myModal_show();
        return;
    }
    let loadingMsg = document.getElementById("loadingMsg");
    console.log("=======convertAudio=======")
    loadingMsg.classList.remove("hide");
    loadingMsg.classList.add("show");
    
    let req_data = {
        yt_link: yt_link.value,
        fileType:fileType
    }
    try {
        const response = await axios.post(api_url, req_data, { responseType: 'blob' });
        console.log("response ======> ok")
        console.log(response)
        // 當接收到前端回傳的檔案時，進行瀏覽器自動下載的動作
        // 當接收到前端回傳的檔案時，進行瀏覽器自動下載的動作
        const contentDisposition = response.headers['content-disposition'];
        const fileName = contentDisposition.split('filename=')[1].replace(/"/g, '');
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', fileName);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        loadingMsg.classList.remove("show");
        loadingMsg.classList.add("hide");
    } catch (error) {
        console.log("error=>" + error);
        loadingMsg.classList.remove("show");
        loadingMsg.classList.add("hide");
        msg.value = "請檢查youtube連結是否正確"
        dynamicStatusClass.value = 'fail';
        successFlag.value = false;
        msgModal.value.myModal_show();
    }
    
    
}
    
async function getData() {
    try {
        const response = await axios.get(api_url)
        Object.assign(ytData, response.data);
    } catch (error) {
        console.log(error);
    }
}


function copyLink(e) {
    let btn_ele = null;
    console.log("target=>"+e.target.tagName)
    if (e.target.tagName.toLowerCase() === 'path') {
        btn_ele = e.target.parentNode.parentNode;
    }
    else if (e.target.tagName.toLowerCase() === 'svg') {
        btn_ele = e.target.parentNode;
    } else if (e.target.tagName.toLowerCase() === 'button') {
        btn_ele = e.target;
    }
    console.log("tagName =>"+btn_ele)
    let btn_id = btn_ele.id;
    if (btn_id != undefined && btn_id != null) {
        let id_data_list = btn_id.split("@");
        let a_id = id_data_list[0] + "@a@" + id_data_list[2];
        let a_ele = document.getElementById(a_id);
        let textToCopy = a_ele.href.trim();
        console.log('textToCopy==>'+textToCopy)
        // 創建一個臨時的textarea元素來複製文字
        var tempTextarea = document.createElement('textarea');
        tempTextarea.value = textToCopy;
        document.body.appendChild(tempTextarea);
        
        // 選擇並複製文字
        tempTextarea.select();
        document.execCommand('copy');
        
        // 刪除臨時元素
        document.body.removeChild(tempTextarea);
    }
}

// 網頁回到頂部
function scrollUp(params) {
    window.scrollTo(0,0)
}

// 登出

function logout() {
    console.log('logout')
    localStorage.removeItem('login')
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    loginStatus.value = false;
    msg.value = '登出成功'
    dynamicStatusClass = 'success'
    successFlag.value = true;
    msgModal.value.myModal_show();
    setTimeout(() => {
        msgModal.value.myModal_hide();
        router.push("/")
    }, 800);
    
}

function parseJwt(token) {
  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
  } catch (e) {
    console.error('Invalid JWT token', e);
    return null;
  }
}

function getUsernameFromToken(token) {
  const payload = parseJwt(token);
  return payload ? payload.username : null;
}

</script>

<style scoped>
/* 通用样式 */
body, html {
    margin: 0;
    padding: 0;
    font-family: 'Arial', sans-serif;
    background-color: #f0f2f5;
    color: #333;
}

.container {
    width: 90%;
    margin: 0 auto;
    padding-top: 20px;
}

/* 页头样式 */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 20px; /* 調整上下20px，左右20px的padding */
    background-color: #ffffff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    position: relative;
}

.title {
    font-size: 1.5em;
    font-weight: bold;
    text-align: center;
    flex-grow: 1;
}

.userblock {
    position: relative;
}

.userblock button.account-btn {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 10px 20px; /* 調整內邊距，使其顯得更寬 */
    border-radius: 30px; /* 設置圓角來實現膠囊形狀 */
    cursor: pointer;
    font-size: 1em;
    margin-right: 10px; /* 右邊距增加 */
    margin-top: 10px; /* 上邊距增加 */
    margin-bottom: 10px; /* 下邊距增加 */
    display: inline-block; /* 設置為行內塊元素，使得寬度根據內容自適應 */
    transition: background-color 0.3s, color 0.3s;
    width: 90px;
}

.userblock button.account-btn:hover {
    background-color: #0056b3; /* 滑鼠移過時變換背景色 */
}


.execBlock {
    display: none;
    position: absolute;
    right: 0;
    top: 100%;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    z-index: 1000;
}

.userblock button.account-btn:focus + .execBlock,
.userblock button.account-btn:active + .execBlock {
    display: block;
}

.execStyle {
    padding: 10px 20px;
    border-bottom: 1px solid #ddd;
    cursor: pointer;
}

.execStyle:last-child {
    border-bottom: none;
}

/* 主体样式 */
.body {
    padding: 20px;
    background-color: #fff;
    margin-top: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.body input[type="text"] {
    width: calc(100% - 30px); /* 減去左右各15px的 padding */
    padding: 15px; /* 左右各15px的 padding */
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-bottom: 20px;
    font-size: 1em;
}

.button-group {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.convertBtn {
    flex: 1;
    padding: 15px;
    margin-right: 10px;
    border: none;
    background-color: #007bff;
    color: #fff;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.3s;
}

.convertBtn:hover {
    background-color: #0056b3;
}

.convertBtn:last-child {
    margin-right: 0;
}

.sub_title {
    font-size: 1.5em;
    margin-bottom: 20px;
    font-weight: bold;
}

/* 推荐区块样式 */
.recommendation {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.music_block {
    flex: 1 1 calc(25% - 20px); /* 調整間距 */
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 20px; /* 保留原有的下邊距 */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    position: relative;
    transition: transform 0.3s, box-shadow 0.3s;
    margin-right: 20px; /* 新增右邊距 */
}

.music_block:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.music_block img {
    width: 100%;
    border-radius: 10px;
}

.music_block a {
    position: absolute;
    top: 10px;
    right: 10px;
    background-color: rgba(0, 0, 0, 0.5);
    color: #fff;
    padding: 5px 10px;
    border-radius: 5px;
    font-size: 0.9em;
    text-decoration: none;
    transition: background-color 0.3s;
}

.music_block a:hover {
    background-color: rgba(0, 0, 0, 0.8);
}

.music_title {
    display: block;
    margin: 10px 0;
    font-size: 1em;
    font-weight: bold;
    color: #007bff;
}

.music_block button {
    position: absolute;
    bottom: 10px;
    right: 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 0.9em;
    transition: background-color 0.3s;
}

.music_block button:hover {
    background-color: #0056b3;
}


.title {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* 使用不同的字體 */
    font-size: 2.5em; /* 調大字體大小 */
    font-weight: bold;
    text-align: center;
    flex-grow: 1;
    color: #007bff; /* 設置顏色為藍色 */
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3); /* 添加文字陰影效果 */
    margin: 0 20px; /* 左右增加一些邊距 */
    padding: 10px; /* 添加內邊距 */
}

/* 等候訊息樣式 */
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

@keyframes bounce {
    0% {
        transform: translateY(0);
    }
    100% {
        transform: translateY(-5px);
    }
}


.hide{
    display: none;
}

.show{
    display: block;
}

/* fab按鈕 */
.fab {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background-color: #4267B2;
    color: #fff;
    border: none;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 30px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    cursor: pointer;
    z-index: 1000;
}

a{
    text-decoration: none;
    color: white;
}

span.username{
    margin: 0px 30px 0px 0px;
    background-color: rgb(213, 29, 103);
    padding: 20px;
    color: #ffffff;
    font-size: 20px;

    border-radius: 50%;
}
.head_icon{
    margin: 10px 20px 0px 10px;
}

.username{
    background-color: rgb(213, 29, 103);
    padding: 20px;
    color: #ffffff;
    font-size: 16px;
    border-radius: 50%;
    position: absolute;
    right: 0px;
    top: 10px;
}
</style>