"""
数据验证模块
"""

from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
from spider.logging_config import setup_logger

logger = setup_logger("validators")


class JobValidator:
    """职位数据验证器"""

    REQUIRED_FIELDS = [
        "id", "enterprise_id", "enterprise_name", "job_title",
        "job_type", "region", "education", "publish_date"
    ]

    VALID_JOB_TYPES = ["全职", "兼职", "实习", "临时", "外包"]
    VALID_EDUCATION = ["不限", "大专", "本科", "硕士", "博士"]
    VALID_REGIONS = [
        "昆明市", "曲靖市", "玉溪市", "保山市", "昭通市",
        "丽江市", "普洱市", "临沧市", "楚雄彝族自治州",
        "红河哈尼族彝族自治州", "文山壮族苗族自治州",
        "西双版纳傣族自治州", "大理白族自治州",
        "德宏傣族景颇族自治州", "怒江傈僳族自治州",
        "迪庆藏族自治州"
    ]

    @classmethod
    def validate(cls, job: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """
        验证单条职位数据

        Args:
            job: 职位数据字典

        Returns:
            (是否有效, 错误信息)
        """
        # 检查必填字段
        for field in cls.REQUIRED_FIELDS:
            if field not in job or job[field] is None or job[field] == "":
                return False, f"缺少必填字段: {field}"

        #验证职位类型
        if job.get("job_type") not in cls.VALID_JOB_TYPES:
            return False, f"无效的职位类型: {job.get('job_type')}"

        # 验证学历要求
        if job.get("education") not in cls.VALID_EDUCATION:
            return False, f"无效的学历要求: {job.get('education')}"

        # 验证地区
        if job.get("region") not in cls.VALID_REGIONS:
            return False, f"无效的地区: {job.get('region')}"

        # 验证日期格式
        try:
            if job.get("publish_date"):
                datetime.strptime(job["publish_date"], "%Y-%m-%d")
        except ValueError:
            return False, f"无效的日期格式: {job.get('publish_date')}"

        # 验证薪资范围
        salary_min = job.get("salary_min")
        salary_max = job.get("salary_max")
        if salary_min is not None and salary_max is not None:
            if salary_min < 0 or salary_max < 0:
                return False, "薪资不能为负数"
            if salary_min > salary_max:
                return False, "最低薪资不能大于最高薪资"

        return True, None

    @classmethod
    def validate_batch(cls, jobs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        批量验证职位数据

        Args:
            jobs: 职位数据列表

        Returns:
            验证失败的数据列表
        """
        invalid_jobs = []
        for job in jobs:
            is_valid, error_msg = cls.validate(job)
            if not is_valid:
                invalid_jobs.append({
                    "job": job,
                    "error": error_msg
                })
                logger.warning(f"职位数据验证失败: {error_msg} - {job.get('id')}")

        if invalid_jobs:
            logger.warning(f"共发现 {len(invalid_jobs)} 条无效职位数据")

        return invalid_jobs


class EnterpriseValidator:
    """企业数据验证器"""

    REQUIRED_FIELDS = ["id", "name", "type", "industry", "region"]

    VALID_TYPES = ["央企", "国企", "事业单位", "民营"]
    VALID_INDUSTRIES = [
        "电力", "烟草", "能源", "矿产", "交通",
        "建筑", "金融", "通信", "医药", "化工",
        "制造", "农业", "旅游", "文化", "教育",
        "卫生", "水利", "环保", "科技", "其他"
    ]

    @classmethod
    def validate(cls, enterprise: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """
        验证单条企业数据

        Args:
            enterprise: 企业数据字典

        Returns:
            (是否有效, 错误信息)
        """
        # 检查必填字段
        for field in cls.REQUIRED_FIELDS:
            if field not in enterprise or enterprise[field] is None or enterprise[field] == "":
                return False, f"缺少必填字段: {field}"

        # 验证企业类型
        if enterprise.get("type") not in cls.VALID_TYPES:
            return False, f"无效的企业类型: {enterprise.get('type')}"

        # 验证行业
        if enterprise.get("industry") not in cls.VALID_INDUSTRIES:
            return False, f"无效的行业: {enterprise.get('industry')}"

        return True, None

    @classmethod
    def validate_batch(cls, enterprises: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        批量验证企业数据

        Args:
            enterprises: 企业数据列表

        Returns:
            验证失败的数据列表
        """
        invalid_enterprises = []
        for ent in enterprises:
            is_valid, error_msg = cls.validate(ent)
            if not is_valid:
                invalid_enterprises.append({
                    "enterprise": ent,
                    "error": error_msg
                })
                logger.warning(f"企业数据验证失败: {error_msg} - {ent.get('id')}")

        if invalid_enterprises:
            logger.warning(f"共发现 {len(invalid_enterprises)} 条无效企业数据")

        return invalid_enterprises