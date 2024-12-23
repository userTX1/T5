import requests
import time
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin
import random
import base64

cdd=''
http = ''
https = ''
def dl7(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global cdd
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        path1 = 'jolokia'
        path2 = 'actuator/jolokia'
        path3 = 'jolokia/list'
        logging.captureWarnings(True)
        aa1 = requests.post(url1 + path1, cookies=s_cookie, proxies=proxies, verify=False, timeout=5)
        aa2 = requests.post(url1 + path2, cookies=s_cookie, proxies=proxies, verify=False, timeout=5)
        if aa1.status_code == 200 and aa2.status_code==200:
            aa3 = requests.get(url1 + path3, cookies=s_cookie, proxies=proxies, verify=False, timeout=5)
            if 'reloadByURL' in aa3.text and aa3.status_code== 200:
                cdd='[+]Jolokia-Realm-JNDI-RCE-1\n'+str(aa3.text)
            elif 'createJNDIRealm' in aa3.text and aa3.status_code== 200:
                cdd = '[+]Jolokia-Realm-JNDI-RCE-1\n' + str(aa3.text)
            else:
                cdd = '[-]漏洞不存在\n'
        else:
            cdd='[-]漏洞不存在\n'
    except Exception as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ Spring JolokiaRCE ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)