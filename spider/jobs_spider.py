"""
招聘信息爬虫
"""

import requests
from bs4 import BeautifulSoup
import time
import random
from datetime import datetime, timedelta
from config import SETTINGS, YUNNAN_REGIONS


class JobsSpider:
    """招聘信息爬虫"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": SETTINGS["user_agent"]
        })

    def crawl_gongpin(self, keyword=""):
        """爬取国聘网招聘信息"""
        jobs = []
        try:
            # 国聘网搜索API（演示）
            url = "https://www.gongpin.com/api/jobs/search"
            params = {
                "keyword": keyword,
                "location": "云南",
                "page": 1,
                "pageSize": 20
            }

            # 演示数据
            job_titles = ["工程师", "技术员", "管理岗", "财务", "行政", "操作工", "设计师", "分析师"]
            for i in range(1, 11):
                job = {
                    "id": f"gp_{int(time.time())}_{i:04d}",
                    "enterprise_id": f"ent_{random.randint(1, 100):04d}",
                    "enterprise_name": f"云南XX{random.choice(['电力', '烟草', '能源', '矿业'])}有限公司",
                    "job_title": random.choice(job_titles),
                    "job_type": random.choice(["全职", "兼职", "实习"]),
                    "region": random.choice(YUNNAN_REGIONS),
                    "salary_min": random.choice([3000, 5000, 8000, 10000, 15000]),
                    "salary_max": random.choice([5000, 8000, 12000, 20000, 25000]),
                    "salary_text": f"{random.choice(['3k-5k', '5k-8k', '8k-12k', '10k-15k', '15k-20k'])}",
                    "education": random.choice(["不限", "大专", "本科", "硕士"]),
                    "experience": random.choice(["不限", "1-3年", "3-5年", "5年以上"]),
                    "recruit_number": random.choice([1, 2, 3, 5, 10]),
                    "job_description": "负责公司相关业务工作，服从工作安排，完成领导交办任务。",
                    "requirement": "身体健康，品行端正，具有相关工作经验优先。",
                    "contact": "请通过官网报名",
                    "publish_date": (datetime.now() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d"),
                    "source": "国聘网",
                    "source_url": "https://www.gongpin.com"
                }
                jobs.append(job)
            time.sleep(SETTINGS["request_delay"])

        except Exception as e:
            print(f"爬取国聘网出错: {e}")

        return jobs

    def crawl_mohrss(self, keyword=""):
        """爬取中国公共招聘网招聘信息"""
        jobs = []
        try:
            # 人社部公共招聘网API（演示）
            url = "http://job.mohrss.gov.cn/api/jobs"
            params = {
                "keyword": keyword,
                "region": "云南",
                "page": 1
            }

            # 演示数据
            job_titles = ["技术员", "管理员", "办事员", "文员", "操作员", "检验员"]
            for i in range(1, 8):
                job = {
                    "id": f"mohrss_{int(time.time())}_{i:04d}",
                    "enterprise_id": f"ent_{random.randint(1, 100):04d}",
                    "enterprise_name": f"云南省{random.choice(YUNNAN_REGIONS)}XX单位",
                    "job_title": random.choice(job_titles),
                    "job_type": "全职",
                    "region": random.choice(YUNNAN_REGIONS),
                    "salary_min": random.choice([2500, 3000, 4000, 5000]),
                    "salary_max": random.choice([4000, 5000, 6000, 8000]),
                    "salary_text": f"{random.choice(['3k-4k', '4k-6k', '5k-8k'])}",
                    "education": random.choice(["不限", "大专", "本科"]),
                    "experience": "不限",
                    "recruit_number": random.choice([1, 2, 3, 5]),
                    "job_description": "事业单位公开招聘，岗位稳定，待遇按国家规定执行。",
                    "requirement": "具有良好的政治素质和职业道德。",
                    "contact": "详见公告",
                    "publish_date": (datetime.now() - timedelta(days=random.randint(1, 15))).strftime("%Y-%m-%d"),
                    "source": "中国公共招聘网",
                    "source_url": "https://job.mohrss.gov.cn"
                }
                jobs.append(job)
            time.sleep(SETTINGS["request_delay"])

        except Exception as e:
            print(f"爬取公共招聘网出错: {e}")

        return jobs

    def crawl_enterprise_careers(self, enterprise_name, career_url):
        """爬取企业官网招聘页"""
        jobs = []
        try:
            # 实际项目中需要根据每个企业的招聘页实现
            # 这里返回演示数据
            job_titles = ["技术工程师", "项目经理", "职能专员", "运维工程师"]
            for i in range(1, 4):
                job = {
                    "id": f"ent_{int(time.time())}_{i:04d}",
                    "enterprise_id": f"ent_{random.randint(1, 100):04d}",
                    "enterprise_name": enterprise_name,
                    "job_title": random.choice(job_titles),
                    "job_type": "全职",
                    "region": random.choice(YUNNAN_REGIONS),
                    "salary_min": random.choice([6000, 8000, 10000, 12000]),
                    "salary_max": random.choice([10000, 15000, 20000, 25000]),
                    "salary_text": f"{random.choice(['8k-12k', '10k-15k', '12k-18k', '15k-20k'])}",
                    "education": random.choice(["本科", "硕士"]),
                    "experience": random.choice(["1-3年", "3-5年"]),
                    "recruit_number": random.choice([1, 2, 3]),
                    "job_description": f"{enterprise_name}诚聘英才，福利待遇优厚。",
                    "requirement": "相关工作经验，具备良好的专业能力。",
                    "contact": "请发送简历至招聘邮箱",
                    "publish_date": (datetime.now() - timedelta(days=random.randint(1, 20))).strftime("%Y-%m-%d"),
                    "source": f"{enterprise_name}官网",
                    "source_url": career_url or "https://example.com"
                }
                jobs.append(job)

        except Exception as e:
            print(f"爬取企业{enterprise_name}招聘页出错: {e}")

        return jobs

    def run(self):
        """运行爬虫"""
        all_jobs = []

        print("正在爬取国聘网...")
        all_jobs.extend(self.crawl_gongpin())

        print("正在爬取中国公共招聘网...")
        all_jobs.extend(self.crawl_mohrss())

        # 云南主要企业
        yunnan_enterprises = [
            ("云南电网", "https://www.yn.csg.cn"),
            ("中国烟草云南公司", "https://www.yn-tobacco.com"),
            ("云南白药", "https://www.yunnanbaiyao.com.cn"),
            ("云南能投", "https://www.cnyeig.com"),
            ("昆明钢铁", "https://www.kmin.com.cn")
        ]

        for name, url in yunnan_enterprises:
            print(f"正在爬取{name}...")
            all_jobs.extend(self.crawl_enterprise_careers(name, url))
            time.sleep(random.uniform(2, 4))

        return all_jobs