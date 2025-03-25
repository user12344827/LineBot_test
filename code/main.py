import logging
from linebot import LineBotApi
from linebot.models import TextSendMessage
import netifaces as ni
from datetime import datetime, timedelta

import os
from dotenv import load_dotenv

load_dotenv()

# 設定 LINE Bot 的channel_access_token
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
user_id = os.getenv("user_id")

# 創建 LineBotApi 對象
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

# broadcast 模式
line_bot_api.broadcast(TextSendMessage(text = "哈囉～～早午晚安～"))

# 配置日誌系統
logging.basicConfig(
    level=logging.INFO, # 設定日誌等級(DEBUG, INFO, WARNING,ERROR, CRITICAL)
    format='%(asctime)s %(message)s', # 設置日誌格式
    handlers=[logging.StreamHandler()] # 輸出至控制台
)

# 創造一個自定義函數，用於通過LINE發送日誌信息
def send_log_to_line(log_message):
    message = TextSendMessage(text=log_message)
    line_bot_api.push_message(user_id, message)

event_time = datetime.now()
taipei = event_time + timedelta(hours=8)
c_time = taipei.strftime(('%y-%m-%d %H:%M:%S'))
    
# 紀錄程序啟動的日誌通過  LINE BOT 發送
logging.info("program started.")
send_log_to_line(f"{c_time}program started.")

# 獲取並打印IP地址
ni.ifaddresses('enp3s0')
ip = ni.ifaddresses('enp3s0')[ni.AF_INET][0]['addr']
logging.info(f"get IP address {ip}.")

send_log_to_line(f"{c_time}get IP address {ip}.")
