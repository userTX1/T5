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
def ty(url,s_cookie=None):
    global uia
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        headers = {"X-Forwarded-For": "127.0.0.1",
                   "X-Originating": "127.0.0.1",
                   "X-Remote-IP": "127.0.0.1",
                   "X-Remote-Addr": "127.0.0.1",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
                   }
        logging.captureWarnings(True)
        gf = requests.post(url + "ServiceDispatcherServlet",cookies=s_cookie, headers=headers,proxies=proxies, verify=False)
        gf.encoding = 'utf-8'
        if '页面出错啦！' in gf.text and gf.status_code == 500 and "抱歉，您请求的页面出错啦" in gf.text and "Content-Type" in gf.text and "BACKGROUND-COLOR" in gf.text:
            uia = "[+]漏洞存在\n"+str(gf.text)
        else:
            uia = "[-]漏洞不存在"
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 用友nc v6.5 反序列化漏洞 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)