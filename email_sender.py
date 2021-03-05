import yamail
import configparser


class EmailSender(object):
    # 自绑定setting.ini
    config = configparser.ConfigParser()
    config.read("setting.ini", encoding="utf-8")
    user = config.get("email", "user")
    auth_code = config.get("email", "auth_code")
    mail_host = config.get("email", "mail_host")
    yam = yamail.SMTP(user=user, password=auth_code, host=mail_host)

    @classmethod
    def send(cls, to, subject, content):
        if to != "":
            try:
                cls.yam.send(to, subject, content)
                return True
            except:
                print("邮箱账号密码错误")
                return False
