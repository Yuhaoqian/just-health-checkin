### JUST 江苏科技大学 每日健康打卡自动化脚本

### 介绍

自动打卡的实现代码在`health_checkin.py`；如何调用脚本可见`example.py`

本文只介绍如何调用程序接口，如需部署自动化定时任务，你可能需要一台Linux服务器，然后了解一下**crontab**的用法；

如果你没有VPS或者不想折腾，可以使用一些云计算平台的Serverless服务，比如说AWS Lambda、腾讯云函数等等。

### 如何使用？

1. 首先需要安装`requirements.txt`中的依赖：

```
pip install -r requirements.txt
```

2. 个人使用

example code:

```
from health_checkin import checkin
checkin('username', 'password')
```

3. 团体使用

在项目根目录中创建文件`users.json`，并把每位同学的username和password按如下格式输入：


```json
[
    {
        "username": "输入同学1的username",
        "password": "输入同学1的password"
    },
    {
        "username": "输入同学2的username",
        "password": "输入同学2的password"
    },
    {
        "username": "输入同学3的username",
        "password": "输入同学3的password"
    }
]
```

如果团体中有更多的学生，继续往下列就行了 :p

example code:

```
import json
from health_checkin import checkin
try:
    with open('users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)
except Exception as e:
    print('INFO: 不存在文件users.json')
else:
    for user in users:
        checkin(user['username'], user['password'])
```






