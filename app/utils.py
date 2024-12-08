import pandas as pd
from pydantic import BaseModel

file_path = "./resource/总名单.xlsx"


df = pd.read_excel(file_path)


class UserInfo(BaseModel):
    account: str
    seat: str
    name: str


def get_user_info_by_account(account: str):
    row = df[df["正式赛账号"] == account]
    row_names = [
        "姓名",
        "座位",
        "正式赛账号",
    ]
    info = row.loc[:, row_names].values[0]
    return info


if __name__ == "__main__":

    info = get_user_info_by_account("CUIT_AI0")
    print(info)
