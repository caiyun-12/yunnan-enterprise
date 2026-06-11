<script setup>
import { ref } from 'vue'
import { NSelect, NInput, NButton, NSpace } from 'naive-ui'

const emit = defineEmits(['search'])

const keyword = ref('')
const selectedRegion = ref(null)
const selectedType = ref(null)
const selectedEducation = ref(null)
const selectedSalary = ref(null)
const selectedJobType = ref(null)

const regions = [
  { label: '全部地区', value: '' },
  { label: '昆明市', value: '昆明市' },
  { label: '曲靖市', value: '曲靖市' },
  { label: '玉溪市', value: '玉溪市' },
  { label: '保山市', value: '保山市' },
  { label: '昭通市', value: '昭通市' },
  { label: '丽江市', value: '丽江市' },
  { label: '普洱市', value: '普洱市' },
  { label: '临沧市', value: '临沧市' },
  { label: '楚雄彝族自治州', value: '楚雄彝族自治州' },
  { label: '红河哈尼族彝族自治州', value: '红河哈尼族彝族自治州' },
  { label: '文山壮族苗族自治州', value: '文山壮族苗族自治州' },
  { label: '西双版纳傣族自治州', value: '西双版纳傣族自治州' },
  { label: '大理白族自治州', value: '大理白族自治州' },
  { label: '德宏傣族景颇族自治州', value: '德宏傣族景颇族自治州' },
  { label: '怒江傈僳族自治州', value: '怒江傈僳族自治州' },
  { label: '迪庆藏族自治州', value: '迪庆藏族自治州' }
]

const enterpriseTypes = [
  { label: '全部类型', value: '' },
  { label: '央企', value: '央企' },
  { label: '国企', value: '国企' },
  { label: '事业单位', value: '事业单位' }
]

const educationOptions = [
  { label: '学历不限', value: '' },
  { label: '不限', value: '不限' },
  { label: '大专', value: '大专' },
  { label: '本科', value: '本科' },
  { label: '硕士', value: '硕士' },
  { label: '博士', value: '博士' }
]

const salaryOptions = [
  { label: '薪资不限', value: '' },
  { label: '面议', value: '面议' },
  { label: '3k以下', value: '0-3000' },
  { label: '3k-5k', value: '3000-5000' },
  { label: '5k-10k', value: '5000-10000' },
  { label: '10k以上', value: '10000-999999' }
]

const jobTypeOptions = [
  { label: '工作性质不限', value: '' },
  { label: '全职', value: '全职' },
  { label: '兼职', value: '兼职' },
  { label: '实习', value: '实习' }
]

const handleSearch = () => {
  emit('search', {
    keyword: keyword.value,
    region: selectedRegion.value,
    type: selectedType.value,
    education: selectedEducation.value,
    salaryRange: selectedSalary.value,
    jobType: selectedJobType.value
  })
}

const handleReset = () => {
  keyword.value = ''
  selectedRegion.value = null
  selectedType.value = null
  selectedEducation.value = null
  selectedSalary.value = null
  selectedJobType.value = null
  emit('search', {
    keyword: '',
    region: '',
    type: '',
    education: '',
    salaryRange: '',
    jobType: ''
  })
}
</script>

<template>
  <div class="bg-white rounded-lg shadow-sm p-4">
    <div class="mb-4">
      <n-input
        v-model:value="keyword"
        placeholder="搜索职位名称、公司名称或地区..."
        size="large"
        clearable
        @keyup.enter="handleSearch"
      />
    </div>

    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-3">
      <n-select
        v-model:value="selectedRegion"
        :options="regions"
        placeholder="地区"
        clearable
      />
      <n-select
        v-model:value="selectedType"
        :options="enterpriseTypes"
        placeholder="企业类型"
        clearable
      />
      <n-select
        v-model:value="selectedEducation"
        :options="educationOptions"
        placeholder="学历要求"
        clearable
      />
      <n-select
        v-model:value="selectedSalary"
        :options="salaryOptions"
        placeholder="薪资范围"
        clearable
      />
      <n-select
        v-model:value="selectedJobType"
        :options="jobTypeOptions"
        placeholder="工作性质"
        clearable
      />
    </div>

    <div class="mt-4 flex justify-end gap-3">
      <n-button @click="handleReset">重置</n-button>
      <n-button type="primary" @click="handleSearch">搜索</n-button>
    </div>
  </div>
</template>