import requests
import time
from bs4 import BeautifulSoup
import logging
import re

uj=''
http = ''
https = ''
cd=''
def a2dl159a(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie=None):
    global uj,cd
    global http,https
    try:
        proxies = {'http': http,
                   'https': https}
        logging.captureWarnings(True)
        aa = requests.get(url1 + '/phpmyadmin/',cookies=s_cookie, proxies=proxies,verify=False, timeout=5)
        if 'phpMyAdmin' in aa.json():
            uj = '[+]漏洞存在\n'
        else:
            uj = '[-]漏洞不存在\n' + cd
    except Exception as aaa:
        uj='[-]端口未开启'
def a2jg859a():
    global uj
    return '--------------------------------------------------\n[ 宝塔phpmyadmin未授权访问漏洞 ]\n\n'+ str (uj)+'\n'
def a2u859a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)
