<template>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" ref="modal">
      <div class="main_modal modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="space msg_icon">
                <font-awesome-icon :icon="['fas', 'paper-plane']" class="fa-4x" style="color: #6fa4ce;" />
            </div>
            <div class="mail_msg">
                驗證信已寄出，請至註冊之信箱收信
            </div>
            <div>
                <button class="field_btn" @click="reSendVerifiedEmail">重寄驗證信</button>
            </div>
          </div>
    
        </div>
      </div>
    </div>
    </template>
    
<script>
export default {
    name : "emailModal"
}
</script>

<script setup>
import { onMounted, ref } from 'vue';
import Modal from 'bootstrap/js/dist/modal';
const modal = ref(null);
const myModal = ref(null);

onMounted(() => {
    myModal.value = new Modal(modal.value);
});

const myModal_show = () => {
    myModal.value.show();
};

const myModal_hide = () => {
    myModal.value.hide();
};

defineExpose({
    myModal_show,
    myModal_hide,
});

const props = defineProps(
{
msg: {
    type: String,
    default:"",
    }
}
)

function reSendVerifiedEmail() {
    
}

</script>

<style scoped>

.custom-modal-dialog {
max-width: 300px;
max-height: 200px;
}

.msg_icon {
display: flex;
justify-content: center;
align-items: center;
}

.msg {
display: flex;
justify-content: center;
align-items: center;
font-size: 22px;
font-weight: 700;
}

div.space{
    margin: 20px 0px;
}

div.main_modal{
    width: 400px;
    height: 250px;
}

.fail{
color:red
}

.success{
color: green;
}

div.mail_msg{
    text-align: center;
    font-size: 20px;
    font-weight: 600;

}
.field_btn {
    background: #2575fc;
    color: #fff;
    border: none;
    padding: 15px;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s ease;
    font-size: 16px;
    width: 350px;
    text-align: center;
}
</style>