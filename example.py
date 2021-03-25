

# example: check-in for a group of students
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


# if you just wanna check-in for yourself
# for example : chcekin('172219605220', '123456')