import requests
from bs4 import BeautifulSoup
import re

jhh=[]
jhh1=[]
def aea1(dg1,faaa):
    af = dg1.replace('.', '!')
    ad = re.match('http://.*?!|https://.*?!|.*?!', af)
    if ad != None:
        ag = ad.group()
        vf = af.replace(ag, '').replace('!', '.').replace('/', '')
        url = 'https://icplishi.com/{}/'.format(vf)
        if faaa==0:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
            response = requests.get(url, headers=headers)
            a2 = BeautifulSoup(response.text, 'html.parser')
            as1 = a2.find('div', {'class': 'module mod-panel'})
            as2 = as1.find_all('td')
            for i in as2:
                af = re.search('target="_blank">.*?</a>', str(i))
                if af != None:
                    jhh.append(af.group().replace('target="_blank">', '').replace('</a>', ''))
def sca1():
    for i in jhh:
        if i not in jhh1:
            jhh1.append(i)
    return jhh1
def qca1():
    jhh.clear()
    jhh1.clear()

