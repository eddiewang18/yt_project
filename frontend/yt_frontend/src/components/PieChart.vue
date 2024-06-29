<template>
<canvas ref="chartCanvas"></canvas>
</template>

<script>

export default {
    name:'PieChart'
}

</script>

<script setup>
import { defineProps, ref, onMounted } from 'vue';
import { Pie, mixins } from 'vue-chart3';

const { reactiveProp } = mixins;

const props = defineProps({
    chartData: {
    type: Object,
    required: true
    },
    options: {
    type: Object,
    default: () => ({
        responsive: true,
        maintainAspectRatio: false
    })
    }
});

const chartCanvas = ref(null);

// Extend Pie class from vue-chart3
const Chart = Pie.extend({
    mixins: [reactiveProp],
    mounted() {
    this.renderChart(this.chartData, this.options);
    }
});

// Create the chart instance
const pieChart = new Chart({
    el: chartCanvas,
    propsData: {
    chartData: props.chartData,
    options: props.options
    }
});

// Load chart data on mounted
onMounted(() => {
    pieChart.render();
});

// Expose necessary data to template
return {
    chartCanvas
};
</script>

<style>
/* Add any necessary styles for your chart canvas */
</style>
