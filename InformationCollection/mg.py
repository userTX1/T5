import requests
from bs4 import BeautifulSoup
import time
import os

wu=[]
def aea4(dg1):
    asaa=dg1
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
    mod = ['/phpinfo.php', '/robots.txt', '/config.php','/db.php']
    for i in mod:
        time.sleep(1)
        url1= asaa+i
        response = requests.get(url1, headers=headers)
        if response.status_code==200:
            wu.append(i+'[+]')
        else:
            wu.append(i+'[-]')
    mod1= ['/www.zip','/wwwroot.rar','/wwwroot.zip','/www.rar','/www.zip','/web.zip','/web.rar']
    for i2 in mod1:
        url2 = asaa+i2
        r = requests.get(url2, headers)
        if r.status_code==200:
            with open(str(i2).replace('/',''), "wb") as code:
                code.write(r.content)
        else:
            wu.append(i2+'[-]')
    qw=os.getcwd()
    for i3 in os.listdir(qw):
        da=['.zip','.rar']
        for i1 in da:
            if i1 in i3:
                wu.append(i3+'[+]')
                add=os.remove(qw+'\\'+i3)
def sca4():
    return wu
def qca4():
    wu.clear()
