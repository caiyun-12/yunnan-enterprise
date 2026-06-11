<script setup>
import { NTag, NButton } from 'naive-ui'
import { formatSalary } from '../utils/format'

const props = defineProps({
  job: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['click'])
</script>

<template>
  <div
    class="bg-white rounded-lg shadow-sm p-4 hover:shadow-md transition-shadow cursor-pointer border border-gray-100"
    @click="emit('click', job)"
  >
    <div class="flex justify-between items-start">
      <div class="flex-1">
        <h3 class="text-lg font-semibold text-gray-800">
          {{ job.job_title }}
        </h3>
        <p class="text-primary-600 mt-1">{{ job.enterprise_name }}</p>
      </div>
      <div class="text-right">
        <span class="text-accent-500 font-semibold">{{ formatSalary(job) }}</span>
      </div>
    </div>

    <div class="mt-3 flex flex-wrap gap-2">
      <n-tag size="small" type="info">
        {{ job.region }}
      </n-tag>
      <n-tag size="small" type="info">
        {{ job.education }}
      </n-tag>
      <n-tag size="small" type="info">
        {{ job.job_type }}
      </n-tag>
      <n-tag v-if="job.experience" size="small" type="info">
        {{ job.experience }}
      </n-tag>
      <n-tag v-if="job.recruit_number" size="small" type="info">
        招{{ job.recruit_number }}人
      </n-tag>
    </div>

    <div class="mt-3 flex justify-between items-center">
      <span class="text-gray-400 text-sm">
        发布于 {{ job.publish_date }}
      </span>
      <n-button text type="primary" size="small">
        查看详情
      </n-button>
    </div>
  </div>
</template>