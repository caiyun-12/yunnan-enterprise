<script setup>
import { computed } from 'vue'
import { NModal, NCard, NTag, NButton, NDescriptions, NDescriptionsItem, NSpace } from 'naive-ui'
import { formatSalary, getTypeColor } from '../utils/format'

const props = defineProps({
  job: {
    type: Object,
    required: true
  },
  enterprises: {
    type: Array,
    default: () => []
  },
  show: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['close'])

const enterprise = computed(() => {
  return props.enterprises.find(e => e.id === props.job.enterprise_id)
})
</script>

<template>
  <n-modal
    :show="show"
    preset="card"
    :title="job.job_title"
    :style="{ width: '600px' }"
    @close="emit('close')"
  >
    <div class="space-y-4">
      <div class="flex items-center justify-between">
        <span class="text-lg font-semibold text-primary-600">
          {{ job.enterprise_name }}
        </span>
        <n-tag v-if="enterprise" :type="getTypeColor(enterprise.type)">
          {{ enterprise.type }}
        </n-tag>
      </div>

      <div class="text-2xl font-bold text-accent-500">
        {{ formatSalary(job) }}
      </div>

      <n-descriptions :column="2" bordered size="small">
        <n-descriptions-item label="工作地区">
          {{ job.region }}
        </n-descriptions-item>
        <n-descriptions-item label="学历要求">
          {{ job.education }}
        </n-descriptions-item>
        <n-descriptions-item label="工作经验">
          {{ job.experience || '不限' }}
        </n-descriptions-item>
        <n-descriptions-item label="招聘人数">
          {{ job.recruit_number || '若干' }}
        </n-descriptions-item>
        <n-descriptions-item label="工作性质">
          {{ job.job_type }}
        </n-descriptions-item>
        <n-descriptions-item label="发布日期">
          {{ job.publish_date }}
        </n-descriptions-item>
      </n-descriptions>

      <div v-if="job.job_description">
        <h4 class="font-semibold text-gray-700 mb-2">职位描述</h4>
        <p class="text-gray-600 whitespace-pre-line">{{ job.job_description }}</p>
      </div>

      <div v-if="job.requirement">
        <h4 class="font-semibold text-gray-700 mb-2">任职要求</h4>
        <p class="text-gray-600 whitespace-pre-line">{{ job.requirement }}</p>
      </div>

      <div v-if="job.contact">
        <h4 class="font-semibold text-gray-700 mb-2">联系方式</h4>
        <p class="text-gray-600">{{ job.contact }}</p>
      </div>

      <div v-if="job.source_url" class="pt-2">
        <a
          :href="job.source_url"
          target="_blank"
          rel="noopener noreferrer"
          class="text-primary-600 hover:text-primary-700"
        >
          查看原文链接 →
        </a>
      </div>
    </div>

    <template #footer>
      <n-space justify="end">
        <n-button @click="emit('close')">关闭</n-button>
        <n-button type="primary" tag="a" :href="job.source_url" target="_blank">
          查看原文
        </n-button>
      </n-space>
    </template>
  </n-modal>
</template>