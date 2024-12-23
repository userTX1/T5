import requests
import time
from bs4 import BeautifulSoup
import logging
import json
import re

cdd=''
http = ''
https = ''
def dl181aq(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie=None):
    global cdd
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        headers = {'x-Forwarded-Host': 'cadichioaaa'}
        logging.captureWarnings(True)
        aa = requests.get(url1,cookies=s_cookie,headers=headers,proxies=proxies,verify=False,timeout=5)
        aa.encoding = 'utf-8'
        cd = BeautifulSoup(aa.text, 'html.parser')
        if 'cadichioaaa' in cd.text :
            cdd='[+]漏洞存在'
        else:
            cdd='[-]漏洞不存在'
    except Exception as aaa:
        cdd='[-]请求错误\n'+str(aaa)
def jg9aaq():
    global cdd
    return '--------------------------------------------------\n[ Host头检测(仅检测x-Forwarded-Host) ]\n\n'+ str (cdd)+'\n'
def u9aaq(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)