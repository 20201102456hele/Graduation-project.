<template>
  <Layer :layer="layer" @confirm="submit" ref="layerDom">
    <el-form :model="form" :rules="rules" ref="ruleForm" label-width="120px" style="margin-right:30px;">
      <el-form-item label="软件名称：" prop="software">
        <el-input v-model="form.software" placeholder="请输入名称"></el-input>
      </el-form-item>


      <el-form-item label="意见：" prop="info">
        <el-input v-model="form.info"  placeholder="请输入意见" ></el-input>
      </el-form-item>

    </el-form>
  </Layer>
</template>

<script lang="ts">
import type { LayerType } from '@/components/layer/index.vue'
import type { Ref } from 'vue'
import type { ElFormItemContext } from 'element-plus/lib/el-form/src/token'
import { defineComponent, ref } from 'vue'
import { addOpinionApi } from '@/api/table'
import { selectData, radioData } from './enum'
import Layer from '@/components/layer/index.vue'
export default defineComponent({
  components: {
    Layer
  },
  props: {
    layer: {
      type: Object,
      default: () => {
        return {
          show: false,
          title: '',
          showButton: true
        }
      }
    }
  },
  setup(props, ctx) {
    const ruleForm: Ref<ElFormItemContext|null> = ref(null)
    const layerDom: Ref<LayerType|null> = ref(null)
    let form = ref({
      software: '',
      user: 'he',
      info: '',
    })
    const rules = {
      software: [{ required: true, message: '请输入软件名称', trigger: 'blur' }],
      info: [{ required: true, message: '请输入反馈意见', trigger: 'blur' }],
    }
    init()
    function init() { // 用于判断新增还是编辑功能
      if (props.layer.row) {
        form.value = JSON.parse(JSON.stringify(props.layer.row)) // 数量量少的直接使用这个转
      } else {

      }
    }
    return {
      form,
      rules,
      layerDom,
      ruleForm,
      selectData,
      radioData
    }
  },

  methods: {

    submit() {
      if (this.ruleForm) {
        this.ruleForm.validate((valid) => {
          if (valid) {
            let params = this.form
            if (this.layer.row) {
              // this.updateForm(params)
            } else {
              this.addForm(params)
            }
          } else {
            return false;
          }
        });
      }
    },
    // 新增提交事件
    addForm(params: object) {
      addOpinionApi(params)
      .then(res => {
        this.$message({
          type: 'success',
          message: '反馈成功'
        })
        this.$emit('getTableData', true)
        this.layerDom && this.layerDom.close()
      })
    },
    // 编辑提交事件
    // updateForm(params: object) {
    //   update(params)
    //   .then(res => {
    //     this.$message({
    //       type: 'success',
    //       message: '编辑成功'
    //     })
    //     this.$emit('getTableData', false)
    //     this.layerDom && this.layerDom.close()
    //   })
    // }
  }
})
</script>

<style lang="scss" scoped>

</style>
