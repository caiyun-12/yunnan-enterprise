"""
巨潮资讯网爬虫 - 上市公司信息
"""

import time
import random
from config import SETTINGS, YUNNAN_REGIONS, create_session_with_retries
from logging_config import setup_logger

logger = setup_logger("cninfo_spider")


class CninfoSpider:
    """巨潮资讯网爬虫"""

    def __init__(self):
        self.session = create_session_with_retries(
            max_retries=SETTINGS["max_retries"],
            backoff_factor=SETTINGS["backoff_factor"]
        )

    def search_listed_companies(self, keyword):
        """搜索上市公司"""
        companies = []
        try:
            # 巨潮资讯网API
            url = "http://www.cninfo.com.cn/api/sysapi/p_sysapi1130"
            params = {
                "keyWord": keyword,
                "plate": "云南",
                "page": 1,
                "pageSize": 20
            }

            # TODO: 实际项目中需要实现真实API调用
            # response = self.session.get(url, params=params, timeout=SETTINGS["timeout"])
            # response.raise_for_status()
            # data = response.json()

            # 演示数据
            demo_companies = [
                {
                    "id": f"listed_{i:04d}",
                    "name": f"云南{keyword}{i}股份有限公司",
                    "credit_code": f"91530000MB{random.randint(100000000, 999999999)}",
                    "type": "国企",
                    "industry": random.choice(["矿业", "电力", "医药", "化工", "农业"]),
                    "region": random.choice(YUNNAN_REGIONS),
                    "status": "上市",
                    "address": f"云南省{random.choice(YUNNAN_REGIONS)}XX路XX号",
                    "source": "巨潮资讯网"
                }
                for i in range(1, 4)
            ]
            companies.extend(demo_companies)
            time.sleep(SETTINGS["request_delay"])
            logger.info(f"搜索上市公司 '{keyword}' 完成，获取 {len(demo_companies)} 条数据")

        except Exception as e:
            logger.error(f"搜索上市公司出错: {e}")

        return companies

    def run(self, keywords=None):
        """运行爬虫"""
        if keywords is None:
            keywords = ["云南", "昆明", "矿业", "电力"]

        all_companies = []
        for keyword in keywords:
            logger.info(f"开始搜索上市公司: {keyword}")
            companies = self.search_listed_companies(keyword)
            all_companies.extend(companies)
            time.sleep(random.uniform(1, 3))

        logger.info(f"上市公司搜索完成，共获取 {len(all_companies)} 条数据")
        return all_companies