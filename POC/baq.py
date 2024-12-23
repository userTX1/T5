import requests
import time
from bs4 import BeautifulSoup
import logging

uj=''
nl=0
http = ''
https = ''
def dl3(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global uj,nl
    global http,https
    try:
        proxies = {'http': http,
                   'https': https}
        logging.captureWarnings(True)
        aa = requests.options(url1,cookies=s_cookie,proxies=proxies,verify=False, timeout=5)
        aa.encoding = 'utf-8'
        for i,i1 in aa.headers.items():
            if 'DELETE' in i1 or 'PUT' in i1 or 'TRACE' in i1:
                uj='[+]允许的请求方法: '+i1
                nl+=1
    except Exception as aaa:
        uj='[-]请求错误\n'+str(aaa)
def jh():
    global nl,uj
    if nl==0:
        uj='[-]未检测到请求方法'
    else:
        nl*=0
def jg88():
    global uj
    return '--------------------------------------------------\n[ 不安全的请求方法(OPTIONS请求) ]\n\n'+ str (uj)+'\n'
def u88(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)