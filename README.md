#云南省央企、国企、事业单位招聘信息查询系统

云南省央企、国企、事业单位招聘信息查询系统，为找工作的人提供招聘信息查询服务。

## 数据来源

- 国聘网 (gongpin.com) - 国务院国资委指导的央企国企专属招聘平台
- 中国公共招聘网 (job.mohrss.gov.cn) - 人社部主办的公共就业服务平台
- 主要央企国企官网 - 国家电网、中国烟草等官网招聘页

## 技术栈

- 前端：Vue3 + Vite + TailwindCSS + Naive UI
- 爬虫：Python + Playwright
- 数据：JSON文件存储
- 部署：Vercel

## 项目结构

```
yunnan-enterprise/
├── .github/workflows/     # GitHub Actions
├── spider/                 # Python爬虫
├── data/                   # JSON数据文件
└── frontend/               # Vue3前端
```

## 本地开发

### 前端开发
```bash
cd frontend
npm install
npm run dev
```

### 运行爬虫
```bash
pip install -r requirements.txt
python spider/run_spider.py
```