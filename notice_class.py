import json
import os
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Notice:
    # 名称
    name: str
    # 是否启用
    enable: bool = True
    # 活动内容
    content: Optional[str] = None
    # 定时任务参数：日 | cron格式
    day: Optional[str] = None
    # 定时任务参数：星期 | cron格式
    day_of_week: Optional[str] = None
    # 定时任务参数：小时 | cron格式
    hour: Optional[str] = None
    # 定时任务参数：分钟 | cron格式
    minute: Optional[str] = None
    # 定时任务参数：开始日期 | 会被自动转化成 yyyy-MM-dd HH:mm:ss
    start_date: Optional[str] = None
    # 定时任务参数：结束日志 | 会被自动转化成 yyyy-MM-dd HH:mm:ss
    end_date: Optional[str] = None
    # 活动持续时间 | 纯数字，单位：分钟
    duration: Optional[int] = None
    # 下次活动时间
    next_time: Optional[str] = None
    # 奖励
    reward: List[str] = None


# 从 JSON 文件加载 Notice 对象列表
def load_notices(file_path: str) -> List[Notice]:
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [Notice(**item) for item in data]
