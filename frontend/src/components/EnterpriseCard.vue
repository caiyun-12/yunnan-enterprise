<script setup>
import { NTag, NButton } from 'naive-ui'
import { getTypeColor } from '../utils/format'

const props = defineProps({
  enterprise: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['click'])
</script>

<template>
  <div
    class="bg-white rounded-lg shadow-sm p-4 hover:shadow-md transition-shadow cursor-pointer border border-gray-100"
    @click="emit('click', enterprise)"
  >
    <h3 class="text-lg font-semibold text-gray-800">
      {{ enterprise.name }}
    </h3>

    <div class="mt-2 flex flex-wrap gap-2">
      <n-tag size="small" :type="getTypeColor(enterprise.type)">
        {{ enterprise.type }}
      </n-tag>
      <n-tag size="small" type="info">
        {{ enterprise.industry }}
      </n-tag>
      <n-tag size="small" type="info">
        {{ enterprise.region }}
      </n-tag>
    </div>

    <p class="text-gray-500 text-sm mt-2 truncate">
      {{ enterprise.address }}
    </p>

    <div class="mt-3 flex justify-between items-center">
      <span class="text-gray-400 text-sm">
        {{ enterprise.status }}
      </span>
      <n-button text type="primary" size="small">
        查看职位
      </n-button>
    </div>
  </div>
</template>