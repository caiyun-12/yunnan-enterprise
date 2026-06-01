"""
数据存储模块
"""

import json
import os
from datetime import datetime
from pathlib import Path


class DataStorage:
    """数据存储类"""

    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def save_enterprises(self, enterprises):
        """保存企业数据"""
        file_path = self.data_dir / "enterprises.json"
        data = {
            "update_time": datetime.now().isoformat(),
            "count": len(enterprises),
            "data": enterprises
        }
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"企业数据已保存: {file_path}, 共{len(enterprises)}条")

    def save_jobs(self, jobs):
        """保存招聘数据"""
        file_path = self.data_dir / "jobs.json"
        data = {
            "update_time": datetime.now().isoformat(),
            "count": len(jobs),
            "data": jobs
        }
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"招聘信息已保存: {file_path}, 共{len(jobs)}条")

    def load_enterprises(self):
        """加载企业数据"""
        file_path = self.data_dir / "enterprises.json"
        if not file_path.exists():
            return []
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("data", [])

    def load_jobs(self):
        """加载招聘数据"""
        file_path = self.data_dir / "jobs.json"
        if not file_path.exists():
            return []
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("data", [])

    def get_all_data(self):
        """获取所有数据"""
        return {
            "enterprises": self.load_enterprises(),
            "jobs": self.load_jobs()
        }