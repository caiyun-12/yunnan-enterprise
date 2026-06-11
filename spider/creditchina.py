"""
国家企业信用信息公示系统爬虫
"""

import time
import random
from config import SETTINGS, YUNNAN_REGIONS, create_session_with_retries
from logging_config import setup_logger

logger = setup_logger("creditchina_spider")


class CreditChinaSpider:
    """国家企业信用信息公示系统爬虫"""

    def __init__(self):
        self.session = create_session_with_retries(
            max_retries=SETTINGS["max_retries"],
            backoff_factor=SETTINGS["backoff_factor"]
        )

    def search_enterprise(self, keyword):
        """搜索企业信息"""
        enterprises = []
        try:
            # 演示数据，实际使用时需要根据官方API调整
            url = f"https://www.creditchina.gov.cn/api/enterprise_search"
            params = {
                "keyword": keyword,
                "region": "云南",
                "page": 1,
                "page_size": 20
            }

            # TODO: 实际项目中需要实现真实API调用
            # response = self.session.get(url, params=params, timeout=SETTINGS["timeout"])
            # response.raise_for_status()
            # data = response.json()

            # 模拟数据
            demo_enterprises = [
                {
                    "id": f"ent_{i:04d}",
                    "name": f"{keyword}_{i}有限公司",
                    "credit_code": f"91530000MAt{random.randint(100000000, 999999999)}",
                    "type": random.choice(["央企", "国企", "事业单位"]),
                    "industry": random.choice(["电力", "烟草", "能源", "交通", "金融"]),
                    "region": random.choice(YUNNAN_REGIONS),
                    "status": "存续",
                    "address": f"云南省{random.choice(YUNNAN_REGIONS)}XX路XX号",
                    "source": "国家企业信用信息公示系统"
                }
                for i in range(1, 6)
            ]
            enterprises.extend(demo_enterprises)
            time.sleep(SETTINGS["request_delay"])
            logger.info(f"搜索关键词 '{keyword}' 完成，获取 {len(demo_enterprises)} 条数据")

        except Exception as e:
            logger.error(f"搜索企业出错: {e}")

        return enterprises

    def get_enterprise_detail(self, credit_code):
        """获取企业详情"""
        try:
            # TODO: 实际项目中需要实现真实API调用
            # url = f"https://www.creditchina.gov.cn/api/enterprise_detail/{credit_code}"
            # response = self.session.get(url, timeout=SETTINGS["timeout"])
            # response.raise_for_status()
            # return response.json()

            return {
                "credit_code": credit_code,
                "business_scope": "各类经营活动",
                "establish_date": "2000-01-01",
                "capital": "10000万元"
            }
        except Exception as e:
            logger.error(f"获取企业详情出错: {e}")
            return None

    def run(self, keywords=None):
        """运行爬虫"""
        if keywords is None:
            keywords = ["云南", "昆明", "电力", "烟草", "能源"]

        all_enterprises = []
        for keyword in keywords:
            logger.info(f"开始搜索关键词: {keyword}")
            enterprises = self.search_enterprise(keyword)
            all_enterprises.extend(enterprises)
            time.sleep(random.uniform(1, 3))

        # 去重
        seen = set()
        unique_enterprises = []
        for ent in all_enterprises:
            if ent["credit_code"] not in seen:
                seen.add(ent["credit_code"])
                unique_enterprises.append(ent)

        logger.info(f"企业搜索完成，共获取 {len(unique_enterprises)} 条唯一数据")
        return unique_enterprises