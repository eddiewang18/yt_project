<template>
    <div>
        <span>近</span>
        <input type="text">
        <span>天</span>
        <button>查詢</button>
    </div>
    <div class="card-content-image">
      <canvas id="ytChart" width="100%" height="380"></canvas>
    </div>
  </template>
  
<script setup>
import Chart from 'chart.js/auto';
import { onMounted } from 'vue';

const dataObj = {
  // labels 為橫軸上的分類，為一個陣列
  labels: [
    '轉檔總次數',
    'mp3轉檔次數',
    'mp4轉檔次數'
  ],
  // datasets資料集為一個陣列，裡面的資料類型為一個一個物件
  datasets: [
    // 物件的屬性有 label 與 data
    {
      // label 為資料分類的名稱
      label: '鋼鐵人',
      //  data 為資料內容，是一個陣列，相同 index 的數值會放在同一個橫軸的分類區間
      data: [10],
    },
    {
      label: '美國隊長',
      data: [20],
    },
    {
      label: '蜘蛛人',
      data: [30],
    },
    {
      label: '其他平均',
      data: [30],
    },
  ],
};
onMounted(() => {
  const ctx = document.getElementById('ytChart');
  let chart = new Chart(ctx, {
    // type 可以是 bar，也可以是 line
    type: 'bar',
    data: dataObj,
    options: {
      responsive: true,
      // 如果不設 maintainAspectRatio,寬度會固定
        maintainAspectRatio: false,
        indexAxis:"y",
      plugins: {
        legend: {
          // datasets裡每一個物件會變成圖例，出現在給定的位置
          position: 'top',
        },
        // 圖表標題
        title: {
          display: true,
          text: 'Youtube影音轉檔次數',
        },
      },
    },
  });
});
</script>


<style scoped>
.card-content-image {
  width: 700px;
  height: 450
}

@media (max-width: 992px) {
  .card-content-image {
    width: 300px;
    height: 200px;
    border: 1px solid red;
  }
}
</style>