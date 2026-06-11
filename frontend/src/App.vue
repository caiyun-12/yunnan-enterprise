<script setup>
import { ref, computed, onMounted } from 'vue'
import SearchBar from './components/SearchBar.vue'
import JobList from './components/JobList.vue'
import JobCard from './components/JobCard.vue'
import { NConfigProvider, NMessageProvider, NDialogProvider } from 'naive-ui'

const allJobs = ref([])
const enterprises = ref([])
const loading = ref(false)
const error = ref(null)

// JSON-LD Structured Data for SEO
const jsonLdSchema = computed(() => {
  const schema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "云南央企国企招聘",
    "description": "提供最新云南国企、央企、事业单位招聘信息查询服务",
    "url": "https://yunnan-enterprise.vercel.app/",
    "potentialAction": {
      "@type": "SearchAction",
      "target": {
        "@type": "EntryPoint",
        "urlTemplate": "https://yunnan-enterprise.vercel.app/?search={search_term_string}"
      },
      "query-input": "required name=search_term_string"
    },
    "publisher": {
      "@type": "Organization",
      "name": "云南央企国企招聘",
      "description": "云南省央企、国企、事业单位招聘信息查询系统"
    }
  }
  return JSON.stringify(schema)
})

const filters = ref({
  keyword: '',
  region: '',
  type: '',
  education: '',
  salaryRange: '',
  jobType: ''
})

const filteredJobs = computed(() => {
  let result = [...allJobs.value]
  const f = filters.value

  if (f.keyword) {
    const kw = f.keyword.toLowerCase()
    result = result.filter(job =>
      job.job_title.toLowerCase().includes(kw) ||
      job.enterprise_name.toLowerCase().includes(kw) ||
      job.region.toLowerCase().includes(kw)
    )
  }

  if (f.region) {
    result = result.filter(job => job.region === f.region)
  }

  if (f.type) {
    result = result.filter(job => {
      const enterprise = enterprises.value.find(e => e.id === job.enterprise_id)
      return enterprise?.type === f.type
    })
  }

  if (f.education) {
    result = result.filter(job => job.education === f.education)
  }

  if (f.salaryRange) {
    result = result.filter(job => {
      if (f.salaryRange === '面议' || !job.salary_min) return true
      const [min, max] = f.salaryRange.split('-').map(Number)
      return job.salary_min >= min && (job.salary_max || 0) <= max
    })
  }

  if (f.jobType) {
    result = result.filter(job => job.job_type === f.jobType)
  }

  return result
})

const updateFilters = (newFilters) => {
  filters.value = { ...filters.value, ...newFilters }
}

const fetchData = async () => {
  loading.value = true
  error.value = null

  try {
    const [jobsRes, enterprisesRes] = await Promise.all([
      fetch('/data/jobs.json'),
      fetch('/data/enterprises.json')
    ])

    const jobsData = await jobsRes.json()
    const enterprisesData = await enterprisesRes.json()

    allJobs.value = jobsData.data || []
    enterprises.value = enterprisesData.data || []
  } catch (e) {
    error.value = '加载数据失败，请刷新重试'
    console.error(e)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchData()
})
</script>

<template>
  <n-config-provider>
    <n-message-provider>
      <n-dialog-provider>
        <!-- JSON-LD Structured Data -->
        <script type="application/ld+json" v-html="jsonLdSchema"></script>

        <div class="min-h-screen bg-gray-50">
          <header class="bg-white shadow-sm">
            <div class="max-w-7xl mx-auto px-4 py-4">
              <h1 class="text-2xl font-bold text-primary-600">
                云南央企国企招聘
              </h1>
              <p class="text-gray-500 text-sm mt-1">
                云南省央企、国企、事业单位招聘信息查询
              </p>
            </div>
          </header>

          <main class="max-w-7xl mx-auto px-4 py-6">
            <div v-if="loading" class="text-center py-12">
              <p class="text-gray-500">加载中...</p>
            </div>

            <div v-else-if="error" class="text-center py-12">
              <p class="text-red-500">{{ error }}</p>
            </div>

            <template v-else>
              <search-bar
                @search="updateFilters"
              />

              <div class="mt-6">
                <job-list
                  :jobs="filteredJobs"
                  :enterprises="enterprises"
                />
              </div>
            </template>
          </main>

          <footer class="bg-white border-t mt-12">
            <div class="max-w-7xl mx-auto px-4 py-4 text-center text-gray-500 text-sm">
              <p>数据来源：国聘网、中国公共招聘网、各企业官网</p>
            </div>
          </footer>
        </div>
      </n-dialog-provider>
    </n-message-provider>
  </n-config-provider>
</template>