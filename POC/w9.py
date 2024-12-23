import requests
import time
from bs4 import BeautifulSoup
import logging
import re

uj=''
http = ''
https = ''
def a2dl15(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global uj
    global http,https
    try:
        proxies = {'http': http,
                   'https': https}
        logging.captureWarnings(True)
        aa = requests.get(url1+'wsutc/begin.do',cookies=s_cookie,proxies=proxies,verify=False, timeout=5)
        bb = requests.get(url1 + 'ws_utc/config.do', cookies=s_cookie, proxies=proxies, verify=False, timeout=5)
        if aa.status_code==200 or bb.status_code==200:
            uj='[+]漏洞存在\nws_utc/config.do\nwsutc/begin.do\n'
        else:
            uj='[-]漏洞不存在\n'
    except Exception as aaa:
        uj='[-]请求错误\n'+str(aaa)
def a2jg85():
    global uj
    return '--------------------------------------------------\n[ Weblogic(CVE-2018-2894) ]\n\n'+ str (uj)+'\n'
def a2u85(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)
