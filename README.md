# 西电晨午晚检自动填报模板 云函数部署

## 项目依赖

+ python 3.6
+ requests
+ yamail

## 配置

### setting.ini

设置发送发邮件用户密码

```ini
[email]
# 用户名
user = xxxxxx@qq.com
# 授权码/密码
auth_code = xxxxxxxxx
# smtp host
mail_host = smtp.qq.com
```

### users.json

分别为学号，密码，邮箱(可使用空串，表示不发送)

````json
[
    {
        "studentId":"1xxxxxxxxxx",
        "password":"xxxxxxxxxx",
        "email":"xxxxxxx@qq.com"
    }
]
````

支持多账号，如

```json
[
    {
        "studentId":"1xxxxxxxxxx",
        "password":"xxxxxxxxxx",
        "email":"xxxxxxx@qq.com"
    },
    {
        "studentId":"1xxxxxxxxxx",
        "password":"xxxxxxxxxx",
        "email":"xxxxxxx@qq.com"
    }
]
```



### data.py

默认为南校区数据，坐标添加了随机值



## 使用方法

1. 下载 `晨午晚检2021模板.zip`

2. 腾讯云->云函数->函数服务->新建

   + 创建方式：自定义创建

   + 运行环境：Python3.6

   + 函数代码：本地上传zip包，选`晨午晚检2021模板.zip`

   + 执行方法：index.main_handler

   + 触发器配置：
     + 触发方式：定时触发
     + 触发周期：自定义触发周期
     + Cron表达式：`0 0 8,14,19 * * * *` 表示每天8/14/19点自动执行

3. 找到该函数->函数管理->函数代码->按配置修改文件->部署
	

4. 快速测试（非必须）：函数服务->找到该函数->触发管理->创建API网关触发器->点击访问路径->函数执行，收到邮件