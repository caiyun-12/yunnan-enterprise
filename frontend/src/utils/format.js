/**
 * 共享工具函数
 */

/**
 * 格式化薪资显示
 * @param {Object} job - 职位对象
 * @returns {string} 格式化后的薪资字符串
 */
export function formatSalary(job) {
  if (!job.salary_min && !job.salary_max) {
    return '薪资面议'
  }
  if (job.salary_text) {
    return job.salary_text
  }
  return `${(job.salary_min || 0) / 1000}k-${(job.salary_max || 0) / 1000}k`
}

/**
 * 获取企业类型对应的颜色
 * @param {string} type - 企业类型
 * @returns {string} naive-ui tag type
 */
export function getTypeColor(type) {
  const colors = {
    '央企': 'error',
    '国企': 'warning',
    '事业单位': 'success'
  }
  return colors[type] || 'default'
}