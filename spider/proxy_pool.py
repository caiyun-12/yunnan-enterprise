"""
代理池模块
"""

import random
import time
from typing import Optional, List
from spider.logging_config import setup_logger

logger = setup_logger("proxy_pool")


class ProxyPool:
    """代理池管理器"""

    def __init__(self, proxies: List[str] = None):
        """
        初始化代理池

        Args:
            proxies: 代理列表，格式为 ["http://user:pass@host:port", ...]
        """
        self.proxies = proxies or []
        self.current_index = 0
        self.failed_proxies = set()
        self.proxy_stats = {}  # 记录每个代理的成功失败次数

    def add_proxy(self, proxy: str):
        """添加代理到池中"""
        if proxy not in self.proxies:
            self.proxies.append(proxy)
            logger.info(f"添加代理到池中: {proxy}")

    def remove_proxy(self, proxy: str):
        """从池中移除代理"""
        if proxy in self.proxies:
            self.proxies.remove(proxy)
            logger.info(f"从池中移除代理: {proxy}")

    def get_random_proxy(self) -> Optional[str]:
        """随机获取一个可用代理"""
        available = [p for p in self.proxies if p not in self.failed_proxies]
        if not available:
            logger.warning("代理池为空或所有代理都已失败")
            return None
        return random.choice(available)

    def get_next_proxy(self) -> Optional[str]:
        """循环获取下一个代理"""
        if not self.proxies:
            return None

        # 尝试找到一个可用的代理
        attempts = 0
        while attempts < len(self.proxies):
            proxy = self.proxies[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.proxies)
            attempts += 1

            if proxy not in self.failed_proxies:
                return proxy

        logger.warning("所有代理都已失败")
        return None

    def mark_proxy_failed(self, proxy: str):
        """标记代理为失败"""
        self.failed_proxies.add(proxy)
        if proxy in self.proxy_stats:
            self.proxy_stats[proxy]["failures"] += 1
        else:
            self.proxy_stats[proxy] = {"successes": 0, "failures": 1}
        logger.warning(f"代理失败标记: {proxy}")

    def mark_proxy_success(self, proxy: str):
        """标记代理为成功"""
        if proxy in self.failed_proxies:
            self.failed_proxies.discard(proxy)
        if proxy in self.proxy_stats:
            self.proxy_stats[proxy]["successes"] += 1
        else:
            self.proxy_stats[proxy] = {"successes": 1, "failures": 0}
        logger.debug(f"代理成功: {proxy}")

    def reset_failed_proxies(self):
        """重置所有失败的代理"""
        self.failed_proxies.clear()
        logger.info("已重置所有失败的代理")

    def get_stats(self) -> dict:
        """获取代理使用统计"""
        return {
            "total": len(self.proxies),
            "available": len([p for p in self.proxies if p not in self.failed_proxies]),
            "failed": len(self.failed_proxies),
            "stats": self.proxy_stats
        }

    def get_proxy_dict(self, proxy: str) -> dict:
        """将代理字符串转换为 requests 需要的字典格式"""
        if proxy.startswith("http://"):
            return {"http": proxy, "https": proxy}
        elif proxy.startswith("https://"):
            return {"https": proxy}
        else:
            return {"http": f"http://{proxy}", "https": f"https://{proxy}"}


class FreeProxyGetter:
    """免费代理获取器（需要配合实际API使用）"""

    # 常用免费代理API（示例，实际使用时可能需要更新）
    PROXY_APIS = [
        "https://www.proxy.com/list",
        # 添加其他免费代理API
    ]

    @classmethod
    def fetch_proxies(cls, count: int = 10) -> List[str]:
        """
        从免费代理API获取代理列表

        Args:
            count: 需要获取的代理数量

        Returns:
            代理列表
        """
        proxies = []

        # TODO: 实际项目中需要实现真实API调用
        # 这里使用示例数据
        logger.info(f"从API获取代理，当前实现为演示模式")

        #演示代理数据
        demo_proxies = [
            f"http://user:pass@proxy{i}.example.com:8080"
            for i in range(1, count + 1)
        ]

        proxies.extend(demo_proxies)
        logger.info(f"获取到 {len(proxies)} 个演示用代理")

        return proxies

    @classmethod
    def verify_proxy(cls, proxy: str, timeout: int = 5) -> bool:
        """
        验证代理是否可用

        Args:
            proxy: 代理地址
            timeout: 超时时间（秒）

        Returns:
            是否可用
        """
        import requests
        try:
            response = requests.get(
                "https://httpbin.org/ip",
                proxies={"http": proxy, "https": proxy},
                timeout=timeout
            )
            return response.status_code == 200
        except Exception as e:
            logger.debug(f"代理验证失败 {proxy}: {e}")
            return False