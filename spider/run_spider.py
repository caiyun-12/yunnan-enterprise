"""
爬虫入口
"""

import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from spider.creditchina import CreditChinaSpider
from spider.cninfo import CninfoSpider
from spider.jobs_spider import JobsSpider
from spider.storage import DataStorage


def main():
    """主函数"""
    print("=" * 50)
    print("云南省招聘信息爬虫开始运行")
    print("=" * 50)

    storage = DataStorage()

    # 爬取企业信息
    print("\n[1/3] 爬取企业信息...")
    credit_spider = CreditChinaSpider()
    enterprises = credit_spider.run(keywords=["云南", "昆明", "电力", "烟草", "能源", "矿业"])
    print(f"获取企业信息: {len(enterprises)}条")

    cninfo_spider = CninfoSpider()
    listed_companies = cninfo_spider.run(keywords=["云南", "昆明", "矿业", "电力"])
    print(f"获取上市公司信息: {len(listed_companies)}条")

    all_enterprises = enterprises + listed_companies
    storage.save_enterprises(all_enterprises)

    # 爬取招聘信息
    print("\n[2/3] 爬取招聘信息...")
    jobs_spider = JobsSpider()
    jobs = jobs_spider.run()
    print(f"获取招聘信息: {len(jobs)}条")
    storage.save_jobs(jobs)

    print("\n[3/3] 完成!")
    print("=" * 50)


if __name__ == "__main__":
    main()