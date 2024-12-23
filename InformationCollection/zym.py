import requests
from bs4 import BeautifulSoup
import re

jh=[]
def aea(dg1,faaa):
    af = dg1.replace('.', '!')
    ad = re.match('http://.*?!|https://.*?!|.*?!', af)
    if ad != None:
        ag = ad.group()
        vf = af.replace(ag, '').replace('!', '.').replace('/', '')
        url = 'https://chaziyu.com/{}/'.format(vf)
        try:
            if faaa == 0:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
                response = requests.get(url, headers=headers)
                a2 = BeautifulSoup(response.text, 'html.parser')
                as1 = a2.find('div', {'class': 'result'})
                as2 = as1.find_all('a')
                for i in as2:
                    af = re.search('target="_blank">.*?</a>', str(i))
                    if af != None:
                        rf = af.group().replace('target="_blank">', '').replace('</a>', '').replace('ipchaxun.com',
                                                                                                    '').replace(
                            'chaolianjie.com', '')
                        jh.append(rf)
            else:
                pass
        except:
            pass
def sca():
    return jh
def qca():
    jh.clear()

