import json
import random

# 基础数据
job_titles = [
    "电气工程师", "机械工程师", "软件工程师", "财务专员", "人力资源专员",
    "市场专员", "文案策划", "产品经理", "项目经理", "质量管理工程师",
    "采购专员", "行政助理", "法务专员", "审计专员", "数据分析师",
    "电网调度员", "烟叶技术员", "新能源工程师", "冶金工程师", "公路工程师",
    "建筑设计师", "采矿工程师", "水电站运维工程师", "安全管理员", "施工员",
    "造价工程师", "柜员", "信贷专员", "酒店管理", "旅游产品策划",
    "景区讲解员", "Java开发工程师", "前端开发工程师", "UI设计师", "运营专员",
    "技术员", "研究员", "教师", "医生", "护士",
    "市场推广", "客户服务", "仓库管理", "物流专员", "质检员",
    "车间主任", "生产主管", "设备维护", "工艺工程师", "环境工程师",
    "采矿技术员", "地质工程师", "测量工程师", "预算员", "资料员"
]

enterprise_names = [
    "云南电网有限责任公司", "中国烟草总公司云南省公司", "云南省能源投资集团有限公司",
    "昆明钢铁控股有限公司", "云南白药集团股份有限公司", "云南省交通投资建设集团有限公司",
    "中国铁路昆明局集团有限公司", "云南省农村信用社联合社", "云南建投集团有限责任公司",
    "云南省设计院集团有限公司", "云南锡业股份有限公司", "华能澜沧江水电股份有限公司",
    "云南省人才服务中心", "大理旅游集团有限责任公司", "丽江得一集团有限责任公司",
    "云南铜业股份有限公司", "云南铝业股份有限公司", "昆明有色冶金设计研究院",
    "云南省水利水电投资有限公司", "云南机场集团有限责任公司", "云南邮政储蓄银行",
    "中国建设银行云南省分行", "中国工商银行云南省分行", "中国人寿云南省分公司",
    "中国电信云南分公司", "中国移动云南公司", "中国联通云南省分公司"
]

regions = [
    "昆明市", "曲靖市", "玉溪市", "保山市", "昭通市", "丽江市",
    "普洱市", "临沧市", "楚雄彝族自治州", "红河哈尼族彝族自治州",
    "文山壮族苗族自治州", "西双版纳傣族自治州", "大理白族自治州",
    "德宏傣族景颇族自治州", "怒江傈僳族自治州", "迪庆藏族自治州"
]

job_types = ["全职", "兼职", "实习"]
educations = ["不限", "大专", "本科", "硕士", "博士"]
experiences = ["不限", "1年以下", "1-3年", "3-5年", "5-10年", "10年以上"]

industries = [
    "电力", "烟草", "能源", "钢铁", "医药", "交通", "铁路",
    "金融", "建筑", "设计", "采矿", "水电", "旅游", "水利",
    "通信", "银行", "保险", "制造", "化工", "环保"
]

salary_ranges = [
    (3000, 5000), (5000, 8000), (8000, 12000), (12000, 18000),
    (18000, 25000), (25000, 35000), (35000, 50000)
]

sources = [
    "国聘网", "中国公共招聘网", "云南电网官网", "中国烟草官网",
    "云南省能投官网", "昆明钢铁官网", "云南白药官网", "云南省交投官网",
    "中国铁路昆明局官网", "云南省农信社官网", "云南建投官网", "云南省设计院官网"
]

def generate_job(index):
    ent_id = f"ent_{random.randint(1, 100):04d}"
    salary_range = random.choice(salary_ranges)
    has_salary = random.random() > 0.1

    return {
        "id": f"job_{index:05d}",
        "enterprise_id": ent_id,
        "enterprise_name": random.choice(enterprise_names),
        "job_title": random.choice(job_titles),
        "job_type": random.choice(job_types),
        "region": random.choice(regions),
        "salary_min": salary_range[0] if has_salary else None,
        "salary_max": salary_range[1] if has_salary else None,
        "salary_text": f"{salary_range[0]//1000}k-{salary_range[1]//1000}k" if has_salary else "面议",
        "education": random.choice(educations),
        "experience": random.choice(experiences),
        "recruit_number": random.choice([1, 2, 3, 5, 8, 10, 15, 20, 30, 50]),
        "job_description": f"负责相关业务工作，要求具备良好的专业技能和沟通能力。",
        "requirement": f"身体健康，品行端正，服从工作安排，具有相关工作经验优先。",
        "contact": f"0871-{random.randint(60000000, 69999999)}",
        "publish_date": f"2026-{random.randint(1, 5):02d}-{random.randint(1, 28):02d}",
        "source": random.choice(sources),
        "source_url": "https://example.com"
    }

# 生成2000条数据
jobs = [generate_job(i) for i in range(1, 2001)]

data = {
    "update_time": "2026-05-29T00:00:00",
    "count": len(jobs),
    "data": jobs
}

with open("J:/yunnan-enterprise/data/jobs.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"已生成 {len(jobs)} 条招聘数据")