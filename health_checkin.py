import requests
import re
import time
import json
import logging

logging.basicConfig(level=logging.INFO,
        format='%(asctime)s - %(message)s',
        filename='log.txt',
        filemode='a')

def checkin(username, password):

    s = requests.session()

    # --- login ---
    while True:
        try:
            r = s.get('https://5a5b1b9bd1895cb22de8cc64f0cb2b96ids.v.just.edu.cn/cas/login?service=http%3A%2F%2Fmy.just.edu.cn%2F')
            execution = re.search('name="execution" value="(.*?)"', r.text).group(1)    
        except Exception as ex:
            print('error - execution')
        else:
            print('success - execution')
            break
    data = {
        'username':  username,
        'password':  password,
        'execution': execution,
        '_eventId': 'submit'
    }
    s.post('https://5a5b1b9bd1895cb22de8cc64f0cb2b96ids.v.just.edu.cn/cas/login?service=http://my.just.edu.cn%2F', data)
    # --- login end ---


    # --- checkin ---
    tbrq = time.strftime("%Y-%m-%d", time.localtime())
    tjsj = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    glqsrq = "[\"{}\",\"{}\"]".format(tbrq, tbrq)

    template = \
    {'sqrid': '',
    'sqbmid': '',
    'rysf': '1',
    'sqrmc': '',
    'gh': '',
    'sqbmmc': '',
    'sfzh': '',
    'xb': '1',
    'jgshen': '',
    'jgshi': '',
    'lxdh': '',
    'tbrq': tbrq,
    'jrszd': '',
    'jrstzk': '无',
    'sfjchwry': '否',
    'sfyyqryjc': '否',
    'sfyqgzdyqryjc': '否',
    'sfjcysqzrq': '否',
    'jrsfjgzgfxdq': '否',
    'jgzgfxdq': '',
    'sflz': '否',
    'lzsj': '',
    'lzjtgj': '',
    'lzbc': '',
    'sffz': '否',
    'fhzjsj': '',
    'fhzjgj': '',
    'fhzjbc': '',
    'fztztkdd': '',
    'glqsrq': glqsrq,
    'sffr': '否',
    'tw': '36.3',
    'zwtw': '36.2',
    'jrjzdxxdz': '',
    'bz': '',
    '_ext': '{}',
    'tjsj': tjsj}


    def make_data(template):
        while True:
            try:
                r = s.get('https://ec43d80978edf4f14590b58d041fc8baids.v.just.edu.cn/default/work/jkd/jkxxtb/jkxxcj.jsp?_p=YXM9MiZ0PTImZD0xMDEmcD0xJmY9MzAmbT1OJg__&_l=&_t=')
                st = r.text.index('saveDkjl("dl");\r\n\t\t\r\n\t\t$(function() {')
            except Exception as ex:
                print('error')
                continue
            else:
                print('success')
                break

        print('pass')
        # print(r.text)
        ed = r.text.index("$('div[name=sqrid]').sui().setValue(empID);")
        
        substr = r.text[st:ed]
        result = re.finditer('div\[name=(.*?)\]"\)\.sui\(\)\.setValue\(\'(.*?)\'\);', substr)
        data = dict()
        for i in result:
            data[i.group(1)] = i.group(2)
        for k, v in data.items():
            template[k] = v

        return {"entity": template}

    ret = make_data(template.copy())

    while True:
        r = s.post('https://ec43d80978edf4f14590b58d041fc8baids.v.just.edu.cn/default/work/jkd/jkxxtb/com.sudytech.work.suda.jkxxtb.jktbSave.save.biz.ext', json=ret)
        resp = json.loads(r.text)
        flag = resp['res']
        if flag:
            print(f'{ret["entity"]["sqrmc"]} - health checkin successfully!')
            logging.info(f'{ret["entity"]["sqrmc"]} - health checkin successfully!')

            break
