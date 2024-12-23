import requests
import time
from bs4 import BeautifulSoup
import logging

uj=''
http = ''
https = ''
def dl6(dl):
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
        aa = requests.get(url1+'examples/servlets/servlet/SessionExample',cookies=s_cookie,proxies=proxies,verify=False, timeout=5)
        aa.encoding = 'utf-8'
        if 'GET based form:' in aa.text or '会话.示例' in aa.text:
            uj = '[+]漏洞存在\n/examples/servlets/servlet/SessionExample'
        else:
            uj = '[-]漏洞不存在'
    except Exception as aaa:
        uj='[-]请求错误\n'+str(aaa)
def jg82():
    global uj
    return '--------------------------------------------------\n[ Tomcat-examples泄露 ]\n\n'+ str (uj)+'\n'
def u82(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)