<template>
    <div class="title">
        <!--標題，請至中-->
        YT to MP3 and MP4 後台
    </div>
    <div class="sideBar">
        <!--.sideBar 為可收合的側邊menu，裡面的內容為每個功能的連結-->
        <div>
            <!--按下此紐可以展開/收藏 sidebar-->
            <button @click="collapse">
                <font-awesome-icon v-if="isCollapse" :icon="['fas', 'caret-right']" style="color: #b8d2ff;" />
                <font-awesome-icon v-else :icon="['fas', 'caret-left']" style="color: #b8d2ff;" />
            </button>

        </div>
        <div class="func">
            <!--.func為功能-->
            <RouterLink to="/admin/home/analysis02">用戶分析</RouterLink>
        </div>
        <div class="func">
            <!--.func為功能-->
            <RouterLink to="/admin/home/analysis01">影音報表</RouterLink>
            
        </div>

        <div class="func">
            <!--.func為功能-->
            <RouterLink >帳號管理</RouterLink>
        </div>
    </div>
    <div class="container">
        <!--呈現功能的內容區塊-->
        <RouterView></RouterView>
    </div>
</template>

<script>
import {RouterView , RouterLink} from 'vue-router'

export default {
    name:"admin_home"
}

</script>

<script setup>

import {ref} from 'vue'

let isCollapse = ref(false);


function collapse() {
    document.body.classList.toggle('collapsed');
    isCollapse.value = !isCollapse.value;
}


</script>


<style scoped>
/* General Styles */
body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
    color: #333;
}

a {
    text-decoration: none;
    color: inherit;
}

/* Title Styles */
.title {
    text-align: center;
    background-color: #007BFF;
    color: white;
    padding: 20px;
    font-size: 24px;
    font-weight: bold;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Sidebar Styles */
.sideBar {
    position: fixed;
    top: 0;
    left: 0;
    width: 200px;
    height: 100%;
    background-color: #343a40;
    color: white;
    display: flex;
    flex-direction: column;
    transition: width 0.3s;
}

.sideBar button {
    background-color: #343a40;
    color: white;
    border: none;
    padding: 10px;
    text-align: left;
    width: 100%;
    cursor: pointer;
    outline: none;
    border-bottom: 1px solid #454d55;
}

.sideBar button:hover {
    background-color: #454d55;
}

.sideBar .func {
    padding: 10px 20px;
    border-bottom: 1px solid #454d55;
}

.sideBar .func:hover {
    background-color: #454d55;
}

.sideBar .func RouterLink {
    color: white;
    display: block;
    padding: 10px 0;
}

/* Main Content Styles */
.container {
    margin-left: 200px;
    padding: 20px;
    background-color: #ffffff;
    min-height: 100vh;
    transition: margin-left 0.3s;
}

.collapsed .sideBar {
    width: 60px;
}

.collapsed .sideBar button {
    text-align: center;
}

.collapsed .sideBar .func {
    text-align: center;
}

.collapsed .sideBar .func RouterLink {
    display: none;
}

.collapsed .container {
    margin-left: 60px;
}

/* Media Query for Responsiveness */
@media (max-width: 768px) {
    .sideBar {
        width: 60px;
    }

    .container {
        margin-left: 60px;
    }
}

</style>