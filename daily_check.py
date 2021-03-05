import requests
import data


class DailyCheck(object):
    session = requests.sessions.Session()

    def __init__(self):
        self.cookies = dict()

    def check_login(self):
        url = "https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/index"
        r = DailyCheck.session.get(url, cookies=self.cookies)
        if "操作成功" in r.text:
            return True
        else:
            return False

    def login(self, username, password):
        url = "https://xxcapp.xidian.edu.cn/uc/wap/login/check"
        params = {"username": username,
                  "password": password
                  }
        r_login = DailyCheck.session.post(url, data=params)
        self.cookies = requests.utils.dict_from_cookiejar(r_login.cookies)

    def summit(self):
        url = "https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save"
        params = data.Location.location_dict
        r_check = DailyCheck.session.post(
            url, data=params, cookies=self.cookies)
        return r_check.text
