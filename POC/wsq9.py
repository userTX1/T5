import requests
import time
from bs4 import BeautifulSoup
import logging
import re

ujaa=[]
http = ''
https = ''
cd=''
jh=''
def a2dl159(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie=None):
    global cd
    global http,https
    proxies = {'http': http,
               'https': https}
    logging.captureWarnings(True)
    url1 = re.match('.*://.*?:.*?/|.*://.*?/', url1)
    if url1.group() != None:
        yu = [':8802/', ':8801/', ':8800/', ':9000/',':8761/']
        for i in yu:
            try:
                if True:
                    sd = re.search('.*://.*?:(.*?)/', url1.group())
                    df = str(sd)
                    if df != 'None':
                        asa = len(str(sd.group(1))) + 2
                        cd = url1.group()[0:-asa] + i
                    else:
                        cd = url1.group()[0:-1] + i
                aa = requests.get(cd, cookies=s_cookie, proxies=proxies, verify=False, timeout=5)
                if 'General Info' in aa.text:
                    ujaa.append('[+]漏洞存在 ' + cd)
                    break
                else:
                    ujaa.append('[-]漏洞不存在')
            except:
                ujaa.append('[-]漏洞不存在')
def a2jg859():
    global jh
    for i in ujaa:
        if '漏洞存在' in i:
            jh=str(i)
            ujaa.clear()
            break
        else:
            jh='[-]漏洞不存在'
    return '--------------------------------------------------\n[ Spring Eureka未授权访问漏洞 ]\n\n'+ str (jh)+'\n'
def a2u859(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)
