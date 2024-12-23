import requests
from bs4 import BeautifulSoup
import re
yu=''
wu=[]
def aea5(dg1, faaa):
    global yu
    af = dg1.replace('.', '!')
    ad = re.match('http://.*?!|https://.*?!|.*?!', af)
    if ad != None:
        ag = ad.group()
        vf = af.replace(ag, '').replace('!', '.').replace('/', '')
        url1 = 'http://whois.bugscaner.com/{}'.format(vf)
        if faaa==0:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
            response = requests.get(url1, headers=headers)
            dg = BeautifulSoup(response.text, 'html.parser')
            dg1 = dg.find('div', {'class', 'stats_table_91bf7bf'})
            gy = re.findall(
                'The Registry database contains ONLY \.COM, \.NET, \.EDU domains and.*URL of the ICANN WHOIS Data Problem Reporting System: http://wdprs\.internic\.net/',
                str(dg1))
            dg2 = re.findall('<b>.*?<br/></b>', str(gy))
            for i in dg2:
                dga = str(i).replace('<b>', '').replace('<br/></b>', '')
                wu.append(dga)
                if 'Tech Name: ' in dga:
                    yu=dga
def sca5():
    return wu
def qca5():
    wu.clear()
#---------------------------------------------------------------------------------------注册人反查
wu1=[]
def aea6(faaa):
    global yu
    if faaa==0:
        for i in range(1, 6):
            url2 = 'http://whois.bugscaner.com/register/{}/page/{}.py'.format(yu.replace('Tech Name: ', ''), str(i))
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
            response = requests.get(url2, headers=headers)
            dg = BeautifulSoup(response.text, 'html.parser')
            dg1 = dg.find('div', {'class', 'col-md-12'})
            dg2 = dg1.find_all('a')
            for i in dg2:
                if '<img src="' in str(i):
                    pass
                else:
                    yu = re.search('target="_blank">.*?</a>', str(i)).group()
                    dga1 = str(yu).replace('target="_blank">', '').replace('</a>', '')
                    wu1.append(dga1)
    else:
        pass
def sca6():
    return wu1
def qca6():
    global yu
    yu=''
    wu1.clear()