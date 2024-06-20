<template>
    <div class="title">
        YT to MP3 and MP4 後台
    </div>
    <div class="sideBar">
        <!--.sideBar 為可收合的側邊menu-->
        <div class="func">
            <!--.func為功能-->
            數據分析1
        </div>
        <div class="func">
            <!--.func為功能-->
            數據分析2
        </div>
        <div class="func">
            <!--.func為功能-->
            帳號管理
        </div>
    </div>
    <div class="container">
        <!--內容區-->
        <RouterView></RouterView>
    </div>
</template>

<script>
import {RouterView} from 'vue-router'

export default {
    name:"admin_home"
}

</script>

<script setup>


</script>


<style>

</style>