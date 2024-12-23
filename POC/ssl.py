import requests
import re
from bs4 import BeautifulSoup
import logging
import os
import subprocess

uia = ''
http = ''
https = ''
ug=''
iaq=0
def dl201(dl):
    global http,https
    http=dl
    https=dl
def ty(url,s_cookie):
    global uia,iaq
    global http, https,ug
    try:
        proxies = {'http': http,
                   'https': https}
        url = re.match('http://(.*):.*/|https://(.*):.*/|http://(.*?)/|https://(.*?)/', url)
        dra = url.group(1, 2, 3, 4)
        for i in dra:
            if 'None' not in str(i):
                ug=str(i)
        un=os.getcwd()+'\POC\ssl\sslciphercheck.exe -h {} -p 443'.format(ug)
        res = subprocess.Popen(un, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               encoding='gbk')  # 使用管道
        cg1 = res.stdout.read()
        if 'Supported' in str(cg1):
            uia = '[+]漏洞存在\n'+str(cg1)
        else:
            uia = '[-]漏洞不存在'
    except Exception as aaa:
        uia = '[-]格式错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ SSL/TLS Suffers Bar Mitzvah Attack]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)