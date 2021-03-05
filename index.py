from email_sender import EmailSender
from daily_check import DailyCheck
import json


def main_handler(args1, args2):
    dailyCheck = DailyCheck()
    with open("users.json", "r", encoding="utf-8") as f:
        users = json.loads(f.read())
    for user in users:
        dailyCheck.login(user["studentId"], user["password"])
        if dailyCheck.check_login():
            content = dailyCheck.summit()
        else:
            content = "登录失败"
        EmailSender.send(user["email"], "晨午晚检", content)
