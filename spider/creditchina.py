"""
国家企业信用信息公示系统爬虫
"""

import requests
from bs4 import BeautifulSoup
import time
import random
from config import SETTINGS, YUNNAN_REGIONS


class CreditChinaSpider:
    """国家企业信用信息公示系统爬虫"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": SETTINGS["user_agent"]
        })

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

            # 模拟数据，实际项目中需要实现真实爬取
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

        except Exception as e:
            print(f"搜索企业出错: {e}")

        return enterprises

    def get_enterprise_detail(self, credit_code):
        """获取企业详情"""
        try:
            # 实际项目中需要实现真实API调用
            return {
                "credit_code": credit_code,
                "business_scope": "各类经营活动",
                "establish_date": "2000-01-01",
                "capital": "10000万元"
            }
        except Exception as e:
            print(f"获取企业详情出错: {e}")
            return None

    def run(self, keywords=None):
        """运行爬虫"""
        if keywords is None:
            keywords = ["云南", "昆明", "电力", "烟草", "能源"]

        all_enterprises = []
        for keyword in keywords:
            print(f"正在搜索: {keyword}")
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

        return unique_enterprises