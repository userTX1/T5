import requests
import time
from bs4 import BeautifulSoup
import logging


def a():
        logging.captureWarnings(True)
        aa = requests.options(url='https://blog.csdn.net/',verify=False, timeout=5)
        aa.encoding = 'utf-8'
        print(aa.headers)
        if 'Accept-Ranges' in aa.headers:
            print('1')
a()
ad = {
      'X-Frame-Options': '检测到X-Frame-Options未配置', 'X-XSS-Protection': '检测到目标X-XSS-Protection响应头缺失',
      'X-Content-Type-Options': '检测到目标X-Content-Type-Options响应头缺失',
      'Content-Security-Policy': '检测到目标Content-Security-Policy响应头缺失'
      }