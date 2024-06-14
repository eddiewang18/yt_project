<template>

<div class="container">
    <div class="header">
        <div class="title">
            在線Youtube轉mp3、mp4
        </div>
        <div class="userblock">
            <button class="account-btn">
                登入
            </button>
        </div>
    </div>
    <div class="body">
        <div>
            <input type="text" placeholder="請輸入Youtube連結">
        </div>
        <div class="button-group">
            <button class="convertBtn">轉MP3</button>
            <button class="convertBtn">轉MP4</button>
        </div>
        <div>
            <div class="sub_title">
                為你推薦
            </div>
            <div class="recommendation">
                <div class="music_block">
                    <img src="https://i.ytimg.com/vi/zqKoXPHhmsM/hqdefault.jpg" alt="">
                    <a href="https://www.youtube.com/watch?v=zqKoXPHhmsM" target="_blank">連結</a>
                    <span class="music_title">周杰伦- 一路向北『我一路向北 离开有你的季节』 【动态歌词/Pinyin Lyrics】</span>
                    <button>copy連結</button>
                </div>
                <div class="music_block">
                    <img src="https://i.ytimg.com/vi/HwfZt7-1EHg/hqdefault.jpg" alt="">
                    <a href="https://www.youtube.com/watch?v=bu7nU9Mhpyo" target="_blank">連結</a>
                    <span class="music_title">周杰倫 Jay Chou (特別演出: 派偉俊)【告白氣球 Love Confession】O</span>
                    <button>copy連結</button>
                </div>
                <div class="music_block">
                    <img src="https://i.ytimg.com/vi/zqKoXPHhmsM/hqdefault.jpg" alt="">
                    <a href="https://www.youtube.com/watch?v=zqKoXPHhmsM" target="_blank">連結</a>
                    <span class="music_title">周杰伦- 一路向北『我一路向北 离开有你的季节』 【动态歌词/Pinyin Lyrics】</span>
                    <button>copy連結</button>
                </div>
                <div class="music_block">
                    <img src="https://i.ytimg.com/vi/zqKoXPHhmsM/hqdefault.jpg" alt="">
                    <a href="https://www.youtube.com/watch?v=zqKoXPHhmsM" target="_blank">連結</a>
                    <span class="music_title">周杰伦- 一路向北『我一路向北 离开有你的季节』 【动态歌词/Pinyin Lyrics】</span>
                    <button>copy連結</button>
                </div>
            </div>
        </div>
    </div>
</div>


</template>


<script >
export default {
    name:"Home"
}
</script>

<script setup>

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

</style>