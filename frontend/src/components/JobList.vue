<script setup>
import { ref, computed, watch } from 'vue'
import { NPagination } from 'naive-ui'
import JobCard from './JobCard.vue'
import JobDetailModal from './JobDetailModal.vue'

const props = defineProps({
  jobs: {
    type: Array,
    default: () => []
  },
  enterprises: {
    type: Array,
    default: () => []
  }
})

const currentPage = ref(1)
const pageSize = ref(50)
const selectedJob = ref(null)
const showDetail = ref(false)

const totalCount = computed(() => props.jobs.length)

const totalPages = computed(() => Math.ceil(totalCount.value / pageSize.value))

const paginatedJobs = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value
  const end = start + pageSize.value
  return props.jobs.slice(start, end)
})

watch(() => props.jobs, () => {
  currentPage.value = 1
})

const handlePageChange = (page) => {
  currentPage.value = page
}

const handleJobClick = (job) => {
  selectedJob.value = job
  showDetail.value = true
}

const closeDetail = () => {
  showDetail.value = false
  selectedJob.value = null
}
</script>

<template>
  <div>
    <div v-if="jobs.length === 0" class="text-center py-12 bg-white rounded-lg">
      <p class="text-gray-500">未找到匹配的职位</p>
    </div>

    <div v-else>
      <div class="mb-4 text-gray-600">
        共找到 <span class="font-semibold">{{ totalCount }}</span> 个职位
      </div>

      <div class="space-y-4">
        <job-card
          v-for="job in paginatedJobs"
          :key="job.id"
          :job="job"
          @click="handleJobClick"
        />
      </div>

      <div class="mt-6 flex justify-center" v-if="totalPages > 1">
        <n-pagination
          :page="currentPage"
          :page-count="totalPages"
          :page-slot="7"
          @update:page="handlePageChange"
        />
      </div>
    </div>

    <job-detail-modal
      v-if="showDetail && selectedJob"
      :job="selectedJob"
      :enterprises="enterprises"
      :show="showDetail"
      @close="closeDetail"
    />
  </div>
</template>