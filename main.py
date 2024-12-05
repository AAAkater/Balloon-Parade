import re
import socket
from typing import List

from app.config import setting
from app.device import send_to_printer
from app.log import logger
from app.utils import get_seat

ac_users = {}

log_file_path = "./log/info.log"


def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((setting.BALLOON_HOST, setting.BALLOON_PORT))
    logger.info("监听开启")

    try:
        # with open("./log/info.log", "a", encoding="utf-8") as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            # print(data.decode())
            data_decoded = data.decode()
            ac_time: str = re.search(r"time=(.*?),", data_decoded).group(1)
            user_id: str = re.search(r"user=(.*?),", data_decoded).group(1)
            problem_id: str = re.search(r"problem=(.*)$", data_decoded).group(1)

            if user_id not in ac_users:
                ac_users[user_id] = []

            if problem_id in ac_users[user_id]:
                logger.error("重复提交")
                continue
            ac_users[user_id].append(problem_id)
            # 获取座位
            # seat_info = get_seat(user_id)
            # 日志
            log_info = f"同学:{user_id} ,题目:{problem_id} ,时间:{ac_time},座位:"
            # 持久化
            logger.info(log_info)
            send_to_printer(log_info)
            # f.write(log_info + "\n")

    except KeyboardInterrupt:
        logger.info("监听关闭")
    finally:
        client_socket.close()


if __name__ == "__main__":
    tcp_client()
