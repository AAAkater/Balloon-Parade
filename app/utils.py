import pandas as pd

file_path = "./resource/测试人员名单.xlsx"


df = pd.read_excel(file_path)


def get_seat(username: str):
    seat_info = df.loc[df["用户名"] == username, "座位"].values[0]
    return seat_info


if __name__ == "__main__":

    # # 获取所有列名
    # column_names = df.columns.tolist()

    # # 打印所有列名
    # for column_name in column_names:
    #     print(column_name)

    # seat_info = get_seat("测试人员0")
    # print(seat_info)

    log_info = f"同学:test0 ,题目:114514 ,时间:124,座位:4"
    with open("./log/info.log", "a", encoding="utf-8") as f:
        f.write(log_info + "\n")
