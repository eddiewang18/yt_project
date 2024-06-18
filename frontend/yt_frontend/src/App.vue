<template>
    <div class="head_icon"><RouterLink to="/"><font-awesome-icon :icon="['fas', 'house']" class="fa-2x" style="color: #6099fb;" /></RouterLink> </div>
    <RouterView></RouterView>
</template>

<script>

import { RouterLink, RouterView } from 'vue-router'


export default {
    name:"App"
}

</script>

<style scoped>
    .head_icon{
        margin: 10px 20px 0px 10px;
    }
</style>