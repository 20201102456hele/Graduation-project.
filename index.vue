<template>

  <div class="layout-container">


    <el-form :model="ruleForm"  label-width="100px" class="demo-ruleForm" style="margin-top: 20px">
      <el-form-item label="用户名">
        <el-input v-model="ruleForm.name"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm()">查询</el-button>
      </el-form-item>
    </el-form>

    <div class="category" id="main"  style="height: 500px;width: 800px;margin-top: 20px">


    </div>

  </div>
</template>

<script lang="ts" setup>
import { onMounted, reactive, ref} from 'vue'
import {getCommentTypeApi} from '@/api/table'
import * as echarts from 'echarts';


const ruleForm = reactive({
  name: "支付宝"
})


const submitForm = () =>{
  getData(ruleForm.name)
}


const state = reactive({
  dataX: [],
  dataY: []
})

onMounted(()=>{

  getData(ruleForm.name)

})

const getData = (name: string) => {

  getCommentTypeApi(name)
      .then(res => {
        state.dataX = res.data.dataX
        state.dataY = res.data.dataY

        var chartDom = document.getElementById('main');

        var myChart = echarts.init(chartDom);

        var option;

        option = {
          xAxis: {
            type: 'category',
            data: state.dataX
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              data: state.dataY,
              type: 'bar'
            }
          ]
        };

        option && myChart.setOption(option);



      })


}



</script>

<style lang="scss" scoped>

</style>
