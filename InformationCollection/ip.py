import requests
from bs4 import BeautifulSoup
import time
import os
import logging
import threading
import re
import socket

ipp=''
df=[]
li=[]
def a(u,faaa):
    global ipp
    if faaa==0:#是ip 不运行
        url = 'http://www.jsons.cn/nslookup/'
        data = {'txt_url': u}
        a1 = requests.post(url, data,timeout=15)
        a2 = BeautifulSoup(a1.text, 'html.parser')
        a3 = a2.find('table', {'class': 'table table-bordered table-striped'})
        a4 = a3.find_all('td')
        for i in a4:
            asaa = str(i.get_text()).replace(' ', '').replace('\n', '').replace('183.60.82.98', '')
            ip = re.search(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}', asaa)
            if ip != None:
                ipp = ip.group()
            df.append(asaa)
    else:
        ipp=''
def b():
    return df
def c():
    df.clear()
#-------------------------------------------------------------ip url 判断
def pd(faaa,dg1):
    global ipp
    if faaa==0:
        pass
    else:
        ipp=str(dg1)
#-------------------------------------------------------------IP归属地
def rea():
    global ipp
    url = "https://www.ip138.com/iplookup.asp?ip={}&action=2".format(ipp)
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36' }
    response = requests.get(url=url, headers=headers,timeout=15)
    response.encoding = "gb2312"
    html = response.text
    cd=re.finditer('"(ct|prov|city|yunyin)":"(.*?)"',html)
    for match in cd:
        c=match.group()
        li.append(c)
def j11():
    return li
def qc1():
    li.clear()
#-------------------------------------------------------------CDN检测
u=0
ug=''
def cdnjc(url,faaa):
    global ug
    global u
    if faaa==0:#是ip 不运行
        cd3 = url.replace('http://', '')
        cd4 = cd3.replace('https://', '')
        a3 = cd4.replace('/', '')
        addrs = socket.getaddrinfo(a3, None)
        for i in addrs:
            cf = re.search(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}', str(i))
            u += 1
        if u == 1:
            ug = '[-]不存在CDN'
            u *= 0
        else:
            ug = '[+]存在CDN'
            u *= 0
    else:
        pass
def cdnjg():
    global ug
    return ug
def cdnqk():
    global ug
    ug=''
#-------------------------------------------------------------旁站收集1
pza1=[]
def pz1():
    global ipp
    try:
        url = 'https://www.webscan.cc/ip_{}/'.format(ipp)
        proxies = {'http': None, 'https': None}
        logging.captureWarnings(True)
        r = requests.get(url, proxies=proxies, verify=False,timeout=15)
        r1 = BeautifulSoup(r.text, 'html.parser')
        r2 = r1.find('div', {'class': "module mod-recommend"})
        r3 = r2.find_all("li")
        for i in r3:
            c1 = str(i)
            c = re.findall('<span>.*?</span>', c1)
            b = re.findall('<a class="domain" href="/site_.*?/" target="_blank">', c1)
            s1 = str(b)
            c2 = str(c)
            cs = c2[8:-9]
            cs1 = s1[32:-21]
            uia = cs, cs1
            pza1.append(uia)
    except:
        pass
def jkk():
    global pza1
    return pza1
def jrm():
    global pza1
    pza1.clear()
#-------------------------------------------------------------旁站收集2
pza2=[]
def pz2():
    global ipp
    global pza2
    try:
        url1 = 'https://ipchaxun.com/{}/'.format(ipp)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        logging.captureWarnings(True)
        r = requests.post(url1, headers=headers, verify=False,timeout=15)
        r1 = BeautifulSoup(r.text, 'html.parser')
        r2 = r1.find('div', id='J_domain')
        r3 = r2.find_all('a')
        for i in r3:
            c = i.get('href')
            uia1= c
            pza2.append(uia1)
    except:
        pass
def jkk1():
    return pza2
def jrm1():
    global pza2
    pza2.clear()
#-------------------------------------------------------------端口扫描
c1a=threading.Lock()
od=os.getcwd()
cg1=[]
def a1(HOST,PORT):
    global od
    global c1a
    try:
        a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        a.connect((HOST,PORT))
        c1a.acquire()
        cg2='[+]-->'+str(PORT)
        cg1.append(cg2)
        c1a.release()
    except:
        pass
def ja1():
    return cg1
def rm1():
    cg1.clear()
def port1():
    global ipp
    for r in range(1,65535):
       t = threading.Thread(target=a1, args=(ipp,r))
       t.start()
#-------------------------------------------------------------IP重置
def qkll():
    global ipp
    ipp=''