"""
爬虫配置
"""

# 爬虫设置
SETTINGS = {
    "request_delay": 2,  # 请求间隔（秒）
    "max_retries": 3,  # 最大重试次数
    "timeout": 30,  # 请求超时（秒）
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 目标URL
TARGET_URLS = {
    "gongpin": "https://www.gongpin.com",
    "mohrss": "https://job.mohrss.gov.cn",
    "creditchina": "https://www.creditchina.gov.cn"
}

#云南地区编码
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