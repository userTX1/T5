import requests
import time
from bs4 import BeautifulSoup
import logging
from requests import head

uj=''
nl=0
http = ''
https = ''
def dl2(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global uj
    global nl
    try:
        proxies = {'http': http,
                   'https': https}
        headers={'Origin': 'www.baidu.com'}
        logging.captureWarnings(True)
        aa = requests.get(url1,cookies=s_cookie,headers=headers,proxies=proxies,verify=False, timeout=5)
        aa.encoding = 'utf-8'
        for i, i1 in aa.headers.items():
            if 'www.baidu.com' in i1:
                uj = '[+] '+i +':'+ i1+'\n'
                nl += 1
    except Exception as aaa:
        uj='[-]请求错误\n'+str(aaa)
def jh1():
    global nl
    global uj
    if nl==0:
        uj='[-]漏洞不存在'
    else:
        nl*=0
def jg85():
    global uj
    return '--------------------------------------------------\n[ CORS跨域资源共享 ]\n\n'+ str (uj)+'\n'
def u85(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)