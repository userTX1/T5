import requests
import time
from bs4 import BeautifulSoup
import logging
import re

uj=''
http = ''
https = ''
cd=''
def a2dl159a(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie=None):
    global uj,cd
    global http,https
    try:
        proxies = {'http': http,
                   'https': https}
        logging.captureWarnings(True)
        url1=re.match('.*://.*?:.*?/|.*://.*?/',url1)
        if url1.group()!=None:
            if True:
                sd=re.search('.*://.*?:(.*?)/',url1.group())
                df=str(sd)
                if df!='None':
                    asa=len(str(sd.group(1)))+2
                    cd=url1.group()[0:-asa]+':8095/'
                else:
                    cd=url1.group()[0:-1]+':8095/'
            aa = requests.get(cd+'crowd/', cookies=s_cookie, proxies=proxies, verify=False, timeout=5)
            if 'Atlassian Crowd' in aa.text:
                uj = '[+]漏洞存在\n'
            else:
                uj = '[-]漏洞不存在\n'+cd
    except Exception as aaa:
        uj='[-]端口未开启'
def a2jg859a():
    global uj
    return '--------------------------------------------------\n[ Atlassian Crowd未授权访问漏洞 ]\n\n'+ str (uj)+'\n'
def a2u859a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)
