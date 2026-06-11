"""
爬虫配置
"""

import random
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# User-Agent 列表，用于轮换
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
]

# 爬虫设置
SETTINGS = {
    "request_delay": 2,  # 请求间隔（秒）
    "max_retries": 3,  # 最大重试次数
    "timeout": 30,  # 请求超时（秒）
    "backoff_factor": 0.5,  # 重试间隔递进系数
}


def get_random_user_agent() -> str:
    """随机获取一个 User-Agent"""
    return random.choice(USER_AGENTS)


def create_session_with_retries(max_retries: int = None, backoff_factor: float = None) -> requests.Session:
    """
    创建带有重试机制的 Session

    Args:
        max_retries: 最大重试次数
        backoff_factor: 重试间隔递进系数

    Returns:
        配置好的 Session 对象
    """
    if max_retries is None:
        max_retries = SETTINGS["max_retries"]
    if backoff_factor is None:
        backoff_factor = SETTINGS["backoff_factor"]

    session = requests.Session()

    # 配置重试策略
    retry_strategy = Retry(
        total=max_retries,
        backoff_factor=backoff_factor,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=["HEAD", "GET", "OPTIONS", "POST"]
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    # 设置随机 User-Agent
    session.headers.update({
        "User-Agent": get_random_user_agent()
    })

    return session


# 目标URL
TARGET_URLS = {
    "gongpin": "https://www.gongpin.com",
    "mohrss": "https://job.mohrss.gov.cn",
    "creditchina": "https://www.creditchina.gov.cn"
}

# 云南地区编码
YUNNAN_REGIONS = [
    "昆明市", "曲靖市", "玉溪市", "保山市", "昭通市",
    "丽江市", "普洱市", "临沧市", "楚雄彝族自治州",
    "红河哈尼族彝族自治州", "文山壮族苗族自治州",
    "西双版纳傣族自治州", "大理白族自治州",
    "德宏傣族景颇族自治州", "怒江傈僳族自治州",
    "迪庆藏族自治州"
]

# 企业类型
ENTERPRISE_TYPES = ["央企", "国企", "事业单位"]

# 行业分类
INDUSTRIES = [
    "电力", "烟草", "能源", "矿产", "交通",
    "建筑", "金融", "通信", "医药", "化工",
    "制造", "农业", "旅游", "文化", "教育",
    "卫生", "水利", "环保", "科技", "其他"
]