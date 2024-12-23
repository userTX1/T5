import requests
import time
from bs4 import BeautifulSoup
import logging
import re


def a():
    global uj
    global http,https
    try:
        logging.captureWarnings(True)
        aa = requests.get('http://hetongy.newchinalife.com:8089/www/lib/ionic/js/angular/angular-resource.min.js.map',verify=False, timeout=5)
        aa.encoding = 'utf-8'
        cd = BeautifulSoup(aa.text, 'html.parser')
        print(aa.content)
    except Exception as aaa:
        uj='[-]请求错误\n'+str(aaa)
        print(uj)
a()
