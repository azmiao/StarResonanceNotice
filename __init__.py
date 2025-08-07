import os.path
from datetime import datetime, timedelta
from typing import List

from yuiChyan.service import Service
from .notice_class import load_notices, Notice

sv = Service('star_notice', use_exclude=False)

# 当前目录
current_dir = os.path.dirname(__file__)
# 读取配置文件
notice_data_path = os.path.join(current_dir, 'notice_data.json')
notice_data_list: List[Notice] = load_notices(notice_data_path)


# 循环创建定时任务
for notice in notice_data_list:
    if not notice.enable:
        continue
    # 自定义任务ID
    custom_id = f'{notice.name}'
    # 装饰器函数
    @sv.scheduled_job(
        custom_id=custom_id,
        day=notice.day,
        day_of_week=notice.day_of_week,
        hour=notice.hour,
        minute=notice.minute,
        start_date=notice.start_date,
        end_date=notice.end_date
    )
    async def execute_job(_notice=notice):
        # 广播内容
        msg = f'◆星痕通知小助手提醒您：\n{_notice.name}'
        # 详情内容
        if _notice.content:
            msg += '\n' + _notice.content
        # 持续时间
        if _notice.duration:
            # 计算结束时间
            start_time = datetime.now()
            end_time = start_time + timedelta(minutes=_notice.duration)
            time_range = f"{start_time.strftime('%H:%M')}-{end_time.strftime('%H:%M')}"
            msg += f'\n活动时间：{time_range}'
        # 下次时间
        if _notice.next_time:
            msg += f'\n下次时间：{_notice.next_time}'
        # 活动奖励
        if _notice.reward:
            msg += f'\n活动奖励：' + ', '.join(_notice.reward)
        # 广播消息
        await sv.broadcast(msg, 'STAR', interval_time=0.5)
