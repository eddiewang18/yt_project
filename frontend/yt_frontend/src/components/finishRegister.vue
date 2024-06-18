<template>
    <div class="container">
        <div class="head">
            <div class="title">
                您的帳號已開通
            </div>
        </div>
        <div class="body">
            <!-- 立即登入 和 稍後再說 兩個按鈕並排顯示，但彼此之間要保持距離 -->
            <div class="btn">
                <button><RouterLink to="/login">立即登入</RouterLink></button>
            </div>
            <div>
                <button><RouterLink to="/">返回首頁</RouterLink></button>
            </div>
        </div>       
    </div>

</template>


<script>
export default {
    name:"FinishRegister"
}
</script>

<script setup>
import { RouterLink } from 'vue-router'

</script>


<style scoped>
/* 全局样式 */
body {
    font-family: 'Arial', sans-serif;
    background: linear-gradient(to right, #00c6ff, #0072ff);
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
    color: #0072ff;
    text-align: center;
    margin-bottom: 20px;
}

/* 按钮容器样式 */
.body {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
}

/* 按钮样式 */
.body .btn button,
.body div button {
    background: #0072ff;
    color: #fff;
    border: none;
    padding: 15px 25px;
    border-radius: 5px;
    cursor: pointer;
    
    font-size: 16px;
}

.body .btn button:hover,
.body div button:hover {
    background: #005bb5;
}

a{
    text-decoration: none;
    color: white;
}

</style>