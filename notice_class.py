import json
import os
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Notice:
    name: str
    content: Optional[str] = None
    day: Optional[str] = None
    day_of_week: Optional[str] = None
    hour: Optional[str] = None
    minute: Optional[str] = None
    duration: Optional[int] = None
    reward: List[str] = None


# 从 JSON 文件加载 Notice 对象列表
def load_notices(file_path: str) -> List[Notice]:
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [Notice(**item) for item in data]
