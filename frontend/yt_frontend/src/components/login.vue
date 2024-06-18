<template>
    <div class="container">
        <div class="header">
            <div class="title">
                <!--這裡是標題，可以的話幫我設計新穎的樣式-->
                登入YT2MP32MP4
            </div>
        </div>
        <div class="body">
            <div class="form">
                <form action="">
                    <div class="field_block">
                        <div class="field">
                            <input type="email" placeholder="帳號(Email)" v-model="form.email">
                        </div>
                    </div>

                    <div class="field_block">
                        <!--顯示密碼區塊span.showPwd 請與密碼欄位並排，但要保持間距-->
                        <div class="field">
                            <input v-if="showPwd1" type="password" placeholder="密碼"  v-model="form.password" maxlength="20">
                            <input v-else  type="text" placeholder="密碼"  v-model="form.password" maxlength="20">
                            <span class="showPwd">
                                <button id="showPwd1" @click="showPwdFn" type="button">
                                    <font-awesome-icon @click="showPwdFn" v-if="showPwd1" :icon="['fas', 'eye']" style="color: #ffffff;" />
                                    <font-awesome-icon @click="showPwdFn" v-else :icon="['fas', 'eye-slash']" style="color: #ffffff;" />
                                </button>
                            </span>
                        </div>
                    </div>
                    <div class="field_block">
                        <button @click.prevent="login()" class="field_btn">登入</button>
                    </div>                    
                </form>
            </div>
        </div>
        <div class="foot">
            <div>
               <span class="normalTxt">還沒有帳號?</span><span><RouterLink to="/register">註冊</RouterLink></span> 
            </div>
            <div>
               <span><RouterLink >忘記密碼</RouterLink></span> 
            </div>
        </div>
    </div>
    <modal :msg="msg" :dynamicStatusClass="dynamicStatusClass" :successFlag="successFlag" ref="msgModal"></modal>
</template>

<script>
export default {
    name:"login"
}
</script>

<script setup>

import { reactive , ref } from 'vue'
import axios from 'axios'
import modal from './modal.vue'
 
let showPwd1 = ref(true) // 是否顯示密碼

let msgModal = ref(null); // 指向 modal組件
let msg = ref("");
let dynamicStatusClass = ref("");
let successFlag = ref(false);
// 表單數據
let form = reactive({
    email: "",
    password: "",

})

// 顯示密碼
function showPwdFn(e) {
    let target_ele = e.target;
    let btn_ele = null;
    if (target_ele.tagName.toLowerCase()=='svg') { 
        btn_ele = target_ele.parentNode;
    }else if(target_ele.tagName.toLowerCase()=='path') { 
        btn_ele = target_ele.parentNode.parentNode;
    } else if (target_ele.tagName.toLowerCase()=='button') {
        btn_ele = target_ele;
    }

    let id = target_ele.id.trim();
    if (id == "showPwd1") { 
        showPwd1.value = !showPwd1.value;
    }
    else if (id == "showPwd2") { 
        showPwd2.value = !showPwd2.value;
    } 

}


</script>

<style scoped>
/* 全局样式 */
body {
    font-family: 'Arial', sans-serif;
    background: linear-gradient(to right, #6a11cb, #2575fc);
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
.header .title {
    font-size: 24px;
    font-weight: bold;
    color: #2575fc;
    text-align: center;
    margin-bottom: 20px;
}

/* 表单样式 */
.form form {
    display: flex;
    flex-direction: column;
}

/* 字段块样式 */
.field_block {
    margin-bottom: 20px;
}

/* 字段样式 */
.field {
    display: flex;
    align-items: center;
}

.field input, .field select {
    width: calc(100% - 50px);
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
    margin-right: 10px;
}

.field .showPwd {
    display: flex;
    align-items: center;
}

.field .showPwd button {
    background: #2575fc;
    border: none;
    color: #fff;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s ease;
}

.field .showPwd button:hover {
    background: #1a5bbf;
}

/* 字段消息样式 */
.fieldMsg {
    color: red;
    font-size: 14px;
    margin-top: 5px;
}

.fieldMsg1 {
    color: black;
    font-size: 14px;
    margin-top: 5px;
}

.pwdStrongStyle{
    font-weight: bold;
}

/* 按钮样式 */
.field_btn {
    background: #2575fc;
    color: #fff;
    border: none;
    padding: 15px;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s ease;
    font-size: 16px;
    width: 410px;
}



.field_btn:hover {
    background: #1a5bbf;
}

.green{
    color: rgb(23, 217, 23);
}

.brown{
    color: rgb(236, 183, 114);
}

.red{
    color: red;
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

.foot{
    text-align: center;
}

a{
    text-decoration: none;
    font-size: 20px;
    display: inline-block;
    font-weight: 400;
}
.normalTxt{
    font-size: 18px;
    margin: 0px 6px 0px 0px;
}
</style>