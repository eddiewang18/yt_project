<template>
    <div class="container">
        <div class="header">
            <div class="title">
                <!--這裡是標題，可以的話幫我設計新穎的樣式-->
                註冊帳號
            </div>
        </div>
        <div class="body">
            <div class="form">
                <form action="">
                    <!--
                    css style 設計注意事項:
                        1. 每個 field_block區塊之間請保時適當的間距，不要緊貼再一起
                        2. div.field是放置輸入框欄位，div.fieldMsg是當欄位未通過檢核，顯示檢何訊息的區塊
                        3. div.field與div.fieldMsg請保時適當的間距
                        4. div.fieldMsg內的文字請以紅色呈現
                    -->
                    <div class="field_block">
                        <div class="field">
                            <input @blur="checkAc" type="email" placeholder="帳號(Email)" v-model="form.email">
                        </div>
                        <div class="fieldMsg">
                            {{ acMsg }}
                        </div>
                    </div>
                    <div class="field_block">
                        <div class="field">
                            <input @blur="checkName" type="text" placeholder="您的姓名"  v-model="form.username">
                        </div>
                        <div class="fieldMsg">
                            {{nameMsg}}
                        </div>
                    </div>
                    <div class="field_block">
                        <!--顯示密碼區塊span.showPwd 請與密碼欄位並排，但要保持間距-->
                        <div class="field">
                            <input v-if="showPwd1" @blur="checkPwd" @keyup="isPwdStrong" @focus="pwdNote" type="password" placeholder="密碼"  v-model="form.password" maxlength="20">
                            <input v-else @blur="checkPwd" @keyup="isPwdStrong" @focus="pwdNote" type="text" placeholder="密碼"  v-model="form.password" maxlength="20">
                            <span class="showPwd">
                                <button id="showPwd1" @click="showPwdFn" type="button">
                                    <font-awesome-icon @click="showPwdFn" v-if="showPwd1" :icon="['fas', 'eye']" style="color: #ffffff;" />
                                    <font-awesome-icon @click="showPwdFn" v-else :icon="['fas', 'eye-slash']" style="color: #ffffff;" />
                                </button>
                            </span>
                        </div>
                        <div class="fieldMsg1">
                            <span>{{pwdLabel}}</span><span :class="[pwdStyle,'pwdStrongStyle']">{{ pwdStrong }}</span>
                        </div>
                        <div v-if="isCheck" class="fieldMsg">
                            {{pwdMsg}}
                        </div>
                        <div v-else class="fieldMsg">
                            {{pwdNoteMsg}}
                        </div>
                    </div>
                    <div class="field_block">
                        <!--顯示密碼區塊span.showPwd 請與密碼欄位並排，但要保持間距-->
                        <div class="field">
                            <input @keyup="checkEqPwd" @blur="checkAgainPwd" v-if="showPwd2" type="password" placeholder="確認密碼" v-model="form.againPwd" maxlength="20">
                            <input @keyup="checkEqPwd" v-else type="text" placeholder="確認密碼" v-model="form.againPwd" maxlength="20">
                            <span class="showPwd">
                                <button id="showPwd2" @click="showPwdFn" type="button">
                                    <font-awesome-icon @click="showPwdFn" v-if="showPwd2" :icon="['fas', 'eye']" style="color: #ffffff;" />
                                    <font-awesome-icon @click="showPwdFn" v-else :icon="['fas', 'eye-slash']" style="color: #ffffff;" />
                                </button>
                            </span>
                        </div>
                        <div class="fieldMsg">
                            {{againPwdMsg}}
                        </div>
                    </div>
                    <div class="field_block">
                        <div class="field">
                            <input @blur="checkBirthday" type="date" placeholder="您的生日" v-model="form.birthday">
                        </div>
                        <div class="fieldMsg">
                            {{ birthdayMsg }}
                        </div>
                    </div>
                    <div class="field_block">
                        <div class="field">
                            <select name="sex" v-model="form.sex">
                                <option value="F">女</option>
                                <option value="M">男</option>
                            </select>
                        </div>
                        <div class="fieldMsg">

                        </div>
                    </div>
                    <div class="field_block">
                        <button @click.prevent="register()" class="field_btn">註冊</button>
                    </div>                    
                </form>
            </div>
        </div>
    </div>
    <div id="loadingMsg" class="hide">資料處理中，請稍後...</div>
    <modal :msg="msg" :dynamicStatusClass="dynamicStatusClass" :successFlag="successFlag" ref="msgModal"></modal>
</template>

<script>
export default {
    name:"Register"
}
</script>

<script setup>

import { reactive , ref } from 'vue'
import axios from 'axios'
import modal from './modal.vue'
import emailModal from './emailModal.vue'
 

let acMsg = ref("帳號不可空白") // 檢核帳號msg
let nameMsg = ref("姓名不可空白") // 檢核姓名msg
let pwdMsg = ref("密碼不可空白") // 檢核密碼msg
let pwdNoteMsg = ref("密碼最多允許輸入20個字元") // 密碼提醒
let againPwdMsg = ref("確認密碼不可空白") // 檢核 確認密碼訊息
let birthdayMsg = ref("生日不可空白");

let checkMsgs = [
acMsg,nameMsg,pwdMsg,againPwdMsg,birthdayMsg
]
let isCheck = ref(true) // 密碼是否處在檢核狀態
let pwdStyle = ref("")
let showPwd1 = ref(true) // 是否顯示密碼
let pwdLabel = ref("")
let showPwd2 = ref(true) // 是否顯示 確認密碼
let pwdStrong = ref("") // 密碼強度msg

let msgModal = ref(null); // 指向 modal組件
let emailShowModal = ref(null); // 指向emailModal組件
let msg = ref("");
let dynamicStatusClass = ref("");
let successFlag = ref(false);
// 表單數據
let form = reactive({
    email: "",
    username: "",
    password: "",
    againPwd: "",
    birthday: "",
    sex:"F"
})

function checkAc() {
    let msg = "";
    if (form.email.trim().length == 0) {
        msg = "帳號不可空白"
    }
    acMsg.value = msg;
}

function checkName() {
    let msg = "";
    if (form.username.trim().length == 0) {
        msg = "姓名不可空白"
    }
    nameMsg.value = msg;
}

function pwdNote() {
    isCheck.value = false;
}

// 檢查密碼強度
function isPwdStrong() {
    if (form.password.trim().length>0) { 
        pwdLabel.value = "密碼強度:"
        let result = checkPasswordStrength(form.password);
        if (result == "Strong") {
            pwdStrong.value = "強"
            pwdStyle.value = "green"
        }
        else if (result == "Medium") {
            pwdStrong.value = "中"
            pwdStyle.value = "brown"
        }
        else if (result == "Weak") {
            pwdStrong.value = "弱"
            pwdStyle.value = "red"
        }
    } else {
        pwdLabel.value = ""
        pwdStrong.value = "";
    }

}
// 密碼強度標準
function checkPasswordStrength(password) {
        if (password.length === 0) {
            return 'None';
        }

        const lengthCriteria = password.length >= 8;
        const uppercaseCriteria = /[A-Z]/.test(password);
        const lowercaseCriteria = /[a-z]/.test(password);
        const numberCriteria = /\d/.test(password);
        const specialCharCriteria = /[!@#$%^&*(),.?":{}|<>]/.test(password);

        const criteriaCount = [lengthCriteria, uppercaseCriteria, lowercaseCriteria, numberCriteria, specialCharCriteria].filter(Boolean).length;

        if (criteriaCount >= 4) {
            return 'Strong';
        } else if (criteriaCount >= 2) {
            return 'Medium';
        } else {
            return 'Weak';
        }
}

//檢核密碼
function checkPwd() {
    isCheck.value = true;
    let msg = "";
    if (form.password.trim().length == 0 ) { 
        msg = "密碼不可空白"
    }
    pwdMsg.value = msg
}

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
// 檢核確認密碼
function checkAgainPwd() {
    let msg = "";
    let flag = true;
    if (form.againPwd.trim().length == 0) { 
        msg = "確認密碼不可空白"
        flag = false;
    }
    againPwdMsg.value = msg; 
    return flag;
}

// 檢核確認密碼是否與密碼一致
function checkEqPwd() {
    if (checkAgainPwd()) {
        if (form.password.trim() != form.againPwd.trim()) {
            againPwdMsg.value = "密碼與確認密碼不一致"
            return;
        }
        againPwdMsg.value = "";
    }
}

// 檢核生日
function checkBirthday() {
    let msg = "";
    if (form.birthday.trim().length == 0) { 
        msg = "生日不可空白"
    }
    birthdayMsg.value = msg 
}

// 最後檢核
function allCheck() {
    for (let i = 0; i < checkMsgs.length; i++){
        if (checkMsgs[i].value.length > 0) {
            console.log(checkMsgs[i].value)
            return false;
        }
    }
    return true
}

// 註冊
async function register() {
    if (!allCheck()) {
        return false;
    }
    let response = {}
    try {
        let loadingMsg = document.getElementById("loadingMsg");
        loadingMsg.classList.remove("hide");
        loadingMsg.classList.add("show");        
        let api_url = "http://127.0.0.1:8000/account/register/";
        response = await axios.post(api_url, form);
        let email = response.data.email
        loadingMsg.classList.remove("show");
        loadingMsg.classList.add("hide");
        window.location.href = `http://localhost:5173/sendMail/${email}`;
        
    } catch (error) {
        console.log(error)
        console.log('res=>');
        console.log(response)
        msg.value = "錯誤";
        dynamicStatusClass.value = "fail";
        loadingMsg.classList.remove("show");
        loadingMsg.classList.add("hide");
        msgModal.value.myModal_show();
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
</style>