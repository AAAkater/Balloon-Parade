import re
import socket
from typing import List

from app.config import setting
from app.log import logger

ac_users = {}


def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((setting.BALLON_HOST, setting.BALLOON_PORT))
    logger.info("监听开启")

    try:
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

            logger.info(
                f"同学:{user_id} ,第一次成功ac了题目:{problem_id} ,提交时间为:{ac_time}"
            )

    except KeyboardInterrupt:
        logger.info("监听关闭")
    finally:
        client_socket.close()


if __name__ == "__main__":
    tcp_client()
