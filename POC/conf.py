import requests
import time
from bs4 import BeautifulSoup
import logging

uj=''
http = ''
https = ''
def dl5(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global uj
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        logging.captureWarnings(True)
        aa = requests.get(url1+'conf/server.xml',cookies=s_cookie,proxies=proxies,verify=False, timeout=5)
        aa.encoding = 'utf-8'
        if '/docs/config/' in aa.text and '<?xml' in aa.text:
            uj = '[+]漏洞存在\n'+aa.text
        else:
            uj = '[-]漏洞不存在'
    except Exception as aaa:
        uj='[-]请求错误\n'+str(aaa)
def jg81():
    global uj
    return '--------------------------------------------------\n[ conf 目录泄露 ]\n\n'+ str (uj)+'\n'
def u81(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)